import requests

from django import forms

from pages.models import PCCPage


GEOCODE_URL = (
    'http://nominatim.openstreetmap.org/search'
    '?format=json&countrycodes=gb&q=%s'
)
POLICE_URL = (
    'http://data.police.uk/api/locate-neighbourhood'
    '?q=%s,%s'
)

REQUEST_TIMEOUT = 5


class UnexpectedException(Exception):
    pass


class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=254,
        error_messages={
            'required': 'Please enter your postcode'
        }
    )

    def get_geo(self, q):
        geo_resp = requests.get(GEOCODE_URL % q, timeout=REQUEST_TIMEOUT)
        if not geo_resp.ok:
            raise UnexpectedException()

        geo = geo_resp.json()
        if not geo:
            raise forms.ValidationError('No results found for %s' % q)

        return (geo[0]['lat'], geo[0]['lon'])

    def get_police_force(self, q):
        lat, lng = self.get_geo(q)

        police_resp = requests.get(
            POLICE_URL % (lat, lng), timeout=REQUEST_TIMEOUT
        )

        if not police_resp.ok:
            if police_resp.status_code == 404:
                raise forms.ValidationError(
                    "%s isn't a valid postcode in England or Wales" % q
                )
            else:
                raise UnexpectedException()
        police = police_resp.json()
        return police['force']

    def get_pcc(self, q):
        police_force = self.get_police_force(q)

        try:
            return PCCPage.objects.get(slug=police_force)
        except PCCPage.DoesNotExist:
            pass
        return None

    def clean(self):
        q = self.cleaned_data.get('q')
        try:
            self.cleaned_data['pcc'] = self.get_pcc(q)
        except (UnexpectedException, requests.exceptions.Timeout):
            raise forms.ValidationError(
                "There was an error with your request, please try again."
            )

        return self.cleaned_data
