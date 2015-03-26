import hashlib
import urllib

from django.conf import settings


API_URL = '//api.url2png.com/v6/{api_key}/{token}/png/?{options}'


DEFAULT_SETTINGS = getattr(settings, 'URL2PNG_DEFAULT_SETTINGS', {
    'thumbnail_max_width': 300,
    'accept_languages': 'en-gb,en;q=0.8',
    'ttl': 604800,
    'viewport': '1024x768'
})


class Url2Png(object):
    def __init__(self, url):
        super(Url2Png, self).__init__()
        self.url = url

    def make_options(self, options):
        defaults = dict(DEFAULT_SETTINGS)
        defaults.update(options or {})
        defaults['url'] = self.url

        return urllib.urlencode(defaults)

    def build_url(self, options={}):
        # fail silently if URL2PNG_API_KEY is not defined
        if not settings.URL2PNG_API_KEY:
            return ''

        _options = self.make_options(options)

        token = hashlib.md5(
            '?%s%s' % (_options, settings.URL2PNG_SECRET_KEY)
        ).hexdigest()

        return API_URL.format(
            api_key=settings.URL2PNG_API_KEY,
            token=token,
            options=_options
        )
