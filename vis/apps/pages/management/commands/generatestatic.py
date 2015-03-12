import os
import shutil

from django.conf import settings
from django.core.management.base import NoArgsCommand, CommandError
from django.core.management import call_command

STATIC_FOLDER_NAME = os.path.basename(settings.STATIC_ROOT)
FOLDERS_TO_DELETE = [
    [STATIC_FOLDER_NAME, 'admin'],
    [STATIC_FOLDER_NAME, 'django_extensions'],
    [STATIC_FOLDER_NAME, 'fira'],
    [STATIC_FOLDER_NAME, 'wagtailadmin'],
    [STATIC_FOLDER_NAME, 'wagtailembeds'],
    [STATIC_FOLDER_NAME, 'wagtailextra'],
    [STATIC_FOLDER_NAME, 'wagtailforms'],
    [STATIC_FOLDER_NAME, 'wagtailsnippets'],
    [STATIC_FOLDER_NAME, 'wagtailusers']
]

medusa_path = lambda *x: os.path.join(settings.MEDUSA_DEPLOY_DIR, *x)


class Command(NoArgsCommand):

    def handle_noargs(self, **opts):
        # check that static is there
        if not os.path.isdir(settings.STATIC_ROOT):
            raise CommandError(
                'You need to create the production static folder first'
            )

        call_command("staticsitegen", **opts)

        # copy static folder
        shutil.copytree(
            settings.STATIC_ROOT, medusa_path(STATIC_FOLDER_NAME)
        )

        # delete unnecessary folders
        for folder in FOLDERS_TO_DELETE:
            shutil.rmtree(
                medusa_path(*folder)
            )
