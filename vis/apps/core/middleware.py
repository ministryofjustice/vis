from django.conf import settings

# default 30 days
MAX_AGE = getattr(settings, 'CACHE_CONTROL_MAX_AGE', 2592000)


class MaxAgeMiddleware(object):
    def process_response(self, request, response):
        if not hasattr(request, 'user') or request.user.is_authenticated():
            return response
        if request.method not in ('GET', 'HEAD'):
            return response
        if response.get('Content-Type', None) == 'application/json':
            return response

        response['Cache-Control'] = 'max-age=%d' % MAX_AGE
        return response
