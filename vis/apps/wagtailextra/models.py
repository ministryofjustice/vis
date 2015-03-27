from django.db import models, transaction

from wagtail.wagtailcore.models import Page, \
    UserPagePermissionsProxy, PagePermissionTester


from .mixins import JadePageMixin


class VISUserPagePermissionsProxy(UserPagePermissionsProxy):
    def for_page(self, page):
        """Return a PagePermissionTester object that can be used to query whether this user has
        permission to perform specific tasks on the given page"""
        return VISPagePermissionTester(self, page)


class VISPagePermissionTester(PagePermissionTester):
    def can_delete(self):
        if self.page.is_core:
            return False
        return super(VISPagePermissionTester, self).can_delete()

    def can_unpublish(self):
        if self.page.is_core:
            return False
        return super(VISPagePermissionTester, self).can_unpublish()


class BaseVISPage(JadePageMixin, Page):
    is_core = models.BooleanField(default=False, editable=False)

    is_abstract = True

    def permissions_for_user(self, user):
        """
        Return a PagePermissionsTester object defining what actions the user can perform on this page
        """
        user_perms = VISUserPagePermissionsProxy(user)
        return user_perms.for_page(self)

    @transaction.atomic
    def save(self, *args, **kwargs):
        is_new = self.id is None

        if not is_new and self.is_core:
            old_record = self.__class__.objects.get(id=self.id)
            if old_record.slug:
                self.slug = old_record.slug

        super(BaseVISPage, self).save(*args, **kwargs)

    class Meta:
        abstract = True
