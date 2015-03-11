import os
import shutil

from django.conf import settings
from django.core.management.base import NoArgsCommand, CommandError
from django.core.management import call_command


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
            settings.STATIC_ROOT,
            os.path.join('%s/%s') % (
                settings.MEDUSA_DEPLOY_DIR,
                os.path.basename(settings.STATIC_ROOT)
            )
        )
