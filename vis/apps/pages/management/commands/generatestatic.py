import os
import shutil
import sys
import subprocess

from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.mail import EmailMessage

from wagtail.wagtailcore.models import Site


def run(command, **kwargs):
    defaults = {
        'shell': True
    }
    defaults.update(kwargs)

    return_code = subprocess.call(command, **defaults)
    if return_code:
        sys.exit(return_code)


class Command(NoArgsCommand):

    EXPORT_DIR = os.path.join(settings.PROJECT_DIR, settings.EXPORT_ZIP_NAME)

    def create_export_folder_if_necessary(self):
        # create export dir if doesn't exist
        if not os.path.exists(self.EXPORT_DIR):
            os.makedirs(self.EXPORT_DIR)

    def download_site(self):
        site = Site.objects.all()[0]
        domain = site.hostname
        if site.port != 80:
            domain += ':%s' % site.port
        run('cd %s && wget --quiet http://%s/sitemap.xml --output-document - | egrep -o "http://%s[^<]+" | wget -k -x -p -H -e robots=off -i -' % (
            self.EXPORT_DIR, domain, domain
        ))

    def zip_site(self):
        shutil.make_archive(self.EXPORT_DIR, 'zip', self.EXPORT_DIR)

    def email_zip(self):
        mail = EmailMessage(
            subject=settings.EXPORT_EMAIL_SUBJECT,
            body=settings.EXPORT_EMAIL_BODY,
            to=settings.EXPORT_RECIPIENTS
        )
        mail.attach_file('%s.zip' % self.EXPORT_DIR)
        mail.send()

    def handle_noargs(self, **opts):
        self.create_export_folder_if_necessary()
        self.download_site()
        self.zip_site()
        self.email_zip()
