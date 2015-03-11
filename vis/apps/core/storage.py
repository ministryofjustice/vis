from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from django.conf import settings


class GulpManifestStaticFilesStorage(ManifestStaticFilesStorage):

    manifest_name = settings.PROJECT_DIR + 'static/manifest.json'

    def post_process(self, *args, **kwargs):
        pass

    # def file_hash(self, name, content=None):
    #     pass
