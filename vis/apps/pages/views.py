from django.shortcuts import get_object_or_404, redirect

from pages.models import PCCPage

import requests


GEOCODE_URL = ('http://nominatim.openstreetmap.org/search'
               '?format=json&countrycodes=gb&q=%s')
POLICE_URL = ('http://data.police.uk/api/locate-neighbourhood'
              '?q=%s,%s')


def pcc_search(request):
    if request.method == 'POST':
        try:
            q = request.POST.get('q')

            geo = requests.get(GEOCODE_URL % q).json()
            police = requests.get(POLICE_URL % (geo[0]['lat'],
                                                geo[0]['lon'])).json()

            pcc = get_object_or_404(PCCPage, slug=police['force'])

            return redirect(pcc.url)
        except (KeyError, ValueError):
            pass
    return redirect('/')
