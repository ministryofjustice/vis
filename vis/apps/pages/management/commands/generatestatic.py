import os
import shutil
import sys
import subprocess

from django.conf import settings
from django.core.management.base import NoArgsCommand

from boto.s3.connection import S3Connection
from boto.s3.key import Key

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
        if site.port != 80 and site.port != 443:
            domain += ':%s' % site.port
        protocol = 'https' if site.port == 443 else 'http'
        run('cd %s && wget --quiet %s://%s/sitemap.xml --output-document - | egrep -o "%s://%s[^<]+" | wget -k -x -p -H -e robots=off --exclude-domains=api.url2png.com --restrict-file-names=windows -i -' % (
            self.EXPORT_DIR, protocol, domain, protocol, domain
        ))

    def zip_site(self):
        shutil.make_archive(self.EXPORT_DIR, 'zip', self.EXPORT_DIR)

    def upload_zip(self):
        conn = S3Connection(settings.S3_ACCESS_KEY_ID,
                            settings.S3_SECRET_ACCESS_KEY_ID,
                            host='s3-eu-west-1.amazonaws.com')
        bucket = conn.get_bucket(settings.S3_BUCKET_NAME)

        k = Key(bucket)
        k.key = '%s.zip' % settings.EXPORT_ZIP_NAME
        k.set_contents_from_filename('%s.zip' % self.EXPORT_DIR)

    def handle_noargs(self, **opts):
        self.create_export_folder_if_necessary()
        self.download_site()
        self.zip_site()
        self.upload_zip()
