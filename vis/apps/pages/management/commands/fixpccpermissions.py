from django.contrib.auth.models import User
from django.core.management.base import NoArgsCommand
from pages.models import PCCPage


class Command(NoArgsCommand):

    def handle_noargs(self, **opts):
        for page in PCCPage.objects.all():
            if page.owner.username != page.slug:
                try:
                    u = User.objects.get(username=page.slug)
                    page.owner = u
                    print 'Setting owner of %s to %s' % (page.url, u.username)
                    page.save()
                except User.DoesNotExist:
                    print 'You should load the test_users fixture before running' \
                          'this command.'
