from django.contrib.staticfiles.management.commands.collectstatic import Command as collectstatic
from django.core.management import call_command
from django.conf import settings


class Command(collectstatic):

    def handle(self, *args, **options):
        if settings.COMPRESS_ENABLED and settings.COMPRESS_OFFLINE:
            call_command('compress')
        super(Command, self).handle(*args, **options)



