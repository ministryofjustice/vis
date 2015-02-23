from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from requests.exceptions import Timeout
from pages.models import PCCPage

import requests


GEOCODE_URL = ('http://nominatim.openstreetmap.org/search'
               '?format=json&countrycodes=gb&q=%s')
POLICE_URL = ('http://data.police.uk/api/locate-neighbourhood'
              '?q=%s,%s')


def pcc_search(request):
    result = None
    q = None
    error = None
    if request.method == 'POST':
        try:
            q = request.POST.get('q')

            geo_resp = requests.get(GEOCODE_URL % q, timeout=5)
            if not geo_resp.ok:
                raise ValueError()

            geo = geo_resp.json()
            if len(geo) == 0:
                raise ValidationError('No results found for %s' % q)

            police_resp = requests.get(POLICE_URL % (geo[0]['lat'],
                                                geo[0]['lon']), timeout=5)

            if not police_resp.ok:
                if police_resp.status_code == 404:
                    raise ValidationError("%s isn't a valid postcode in England or Wales" % q)
                else:
                    raise ValueError()

            police = police_resp.json()

            result = get_object_or_404(PCCPage, slug=police['force'])

        except ValidationError as ve:
            error = str(ve.message)
        except (KeyError, ValueError, Timeout):
            error = 'something went wrong'
    return render(request, 'pages/result_list.jade',
                  {'result': result,
                   'error': error,
                   'q': q})
