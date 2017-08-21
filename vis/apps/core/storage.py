import json
import os
from urlparse import urldefrag, urlsplit, urlunsplit, unquote
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage, \
    HashedFilesMixin
from django.conf import settings
from collections import OrderedDict


class GulpManifestStaticFilesStorage(ManifestStaticFilesStorage):

    manifest_name = os.path.join(settings.PROJECT_DIR, 'static/manifest.json')

    def post_process(self, *args, **kwargs):
        return []

    def load_manifest(self):
        content = self.read_manifest()
        if content is None:
            return OrderedDict()
        try:
            stored = json.loads(content, object_pairs_hook=OrderedDict)
        except ValueError:
            pass
        else:
            return stored
        raise ValueError("Couldn't load gulp manifest '%s' " %
                         self.manifest_name)

