from django.contrib.auth.models import User
from django.core.management.base import NoArgsCommand

from wagtail.wagtailcore.models import Page
from info.models import GlossaryItem

from bs4 import BeautifulSoup
from django.contrib.contenttypes.models import ContentType

import json

class Command(NoArgsCommand):

    def handle_noargs(self, **opts):
        for page in Page.objects.all():
            page = self.get_specific_page(page)

            self.update_page(page)
            self.update_revision(page)

        for item in GlossaryItem.objects.all():
            item.description = self.fix_content(item.description)
            item.save()


    def get_latest_revision(self, page):
        return page.revisions.order_by('-created_at').first()


    def fix_content(self, content):
        soup = BeautifulSoup(content)
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is not None and href.startswith(('http', 'https', 'www')):
                link['rel'] = 'external'

        return soup.find('body').decode_contents()


    def update_page(self, page):
        if not hasattr(page, 'content'):
            return

        page.content = self.fix_content(page.content)
        page.save()


    def update_revision(self, page):
        latest_revision = self.get_latest_revision(page)

        if not latest_revision:
            return

        data = json.loads(latest_revision.content_json)

        if 'content' not in data:
            return

        data['content'] = self.fix_content(data['content'])

        latest_revision.content_json = json.dumps(data)
        latest_revision.save()


    def get_specific_page(self, page):
        content_type = ContentType.objects.get_for_id(page.content_type_id)
        if isinstance(page, content_type.model_class()):
            # page is already the an instance of the most specific class
            return page
        else:
            return content_type.get_object_for_this_type(id=page.id)
