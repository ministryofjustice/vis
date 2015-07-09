import os
import time

from django.http import JsonResponse
from django.views.generic import View
from django.db import OperationalError
from django.core.cache import get_cache
from django.conf import settings

from redis.exceptions import ConnectionError
import requests
from geopy.geocoders import Bing
from geopy.exc import GeopyError

from pages.models import HomePage
from core.url2png import Url2Png

REQUEST_TIMEOUT = 10


def ping(request):
    return JsonResponse({
        "commit_id": os.environ.get('GIT_SHA', ''),
        "build_date": os.environ.get('DEPLOY_DATETIME', '')
    })


class HealthCheckView(View):

    def get(self, request, *args, **kwargs):
        database_ok = self.is_database_ok()
        cache_ok = self.is_cache_ok()
        png_ok = self.is_url2png_ok()
        bing_ok = self.is_bing_ok()
        policeuk_ok = self.is_policeuk_ok()

        all_ok = all([database_ok, cache_ok, png_ok, bing_ok, policeuk_ok])

        resp = {
            'database': {
                'description': 'Postgres instance',
                'ok': database_ok
            },
            'cache': {
                'description': 'Redis cache',
                'ok': cache_ok
            },
            'url2png': {
                'description': 'url2png API (https://www.url2png.com/)',
                'ok': png_ok
            },
            'bing': {
                'description': 'Bing Maps geolocation API',
                'ok': bing_ok
            },
            'policeuk': {
                'description': (
                    'Police UK API '
                    '(http://data.police.uk/docs/method/neighbourhood-locate/)'
                ),
                'ok': policeuk_ok
            },
            'ok': all_ok
        }

        status = 200
        if not all_ok:
            status = 500

        return JsonResponse(resp, status=status)

    def is_database_ok(self):
        try:
            return HomePage.objects.first() is not None
        except OperationalError:
            return False

    def is_cache_ok(self):
        cache = get_cache('default')
        timestamp = int(time.time())

        try:
            if cache.__class__.__name__ != 'RedisCache':
                return False

            cache.set('healthcheck', timestamp)
            return cache.get('healthcheck') == timestamp
        except ConnectionError:
            return False

    def is_url2png_ok(self):
        u = Url2Png('https://www.gov.uk/robots.txt')
        png = u.build_url()

        try:
            r = requests.get('http:%s' % png, timeout=REQUEST_TIMEOUT)
            return r.status_code < 400
        except requests.exceptions.RequestException:
            return False

    def is_bing_ok(self):
            try:
                geocoder = Bing(settings.BING_API_TOKEN, '%s, UK')
                geo_resp = geocoder.geocode('SW1A 1AA')
                return True
            except GeopyError:
                return False

    def is_policeuk_ok(self):
        url = ('http://data.police.uk/api/locate-neighbourhood'
               '?q=51.50101852416992,-0.14159967005252838')

        try:
            r = requests.get(url, timeout=REQUEST_TIMEOUT)
            return r.status_code < 400
        except requests.exceptions.RequestException:
            return False
