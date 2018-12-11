import requests

from django import forms
from django.conf import settings

from localflavor.gb.forms import GBPostcodeField

from geopy.geocoders import Bing
from geopy.exc import GeopyError


POLICE_URL = (
    'http://data.police.uk/api/locate-neighbourhood'
    '?q=%s,%s'
)

REQUEST_TIMEOUT = 5


class UnexpectedException(Exception):
    pass


class SearchForm(forms.Form):
    q = GBPostcodeField(
        max_length=254,
        error_messages={
            'required': 'Please enter your postcode'
        }
    )
    lat = forms.CharField(required=False)
    lng = forms.CharField(required=False)

    def clean_q(self):
        q = self.cleaned_data.get('q', '')
        q = q.replace(" ", "")
        return q

    def _clean_geo(self):
        lat = self.cleaned_data.get('lat')
        lng = self.cleaned_data.get('lng')

        if not lat or not lng:
            q = self.cleaned_data.get('q')

            try:
                geocoder = Bing(settings.BING_API_TOKEN, '%s, UK')
                geo_resp = geocoder.geocode(q)
            except GeopyError:
                raise UnexpectedException()

            if not geo_resp:
                raise UnexpectedException()

            placename, (lat, lng) = geo_resp

            # Bing Maps API turns a placename of "United Kingdom" for invalid
            # postcodes that _look_ like a valid postcode - e.g. first text
            # part (SW, SE) followed by regex-matching pattern. Along with the
            # placename, it returns a lat/lon of the middle of the country,
            # which is somewhere in Durham.
            if placename == 'United Kingdom':
                raise UnexpectedException()

            self.cleaned_data['lat'] = lat
            self.cleaned_data['lng'] = lng

        return (lat, lng)

    def _get_police_force(self, lat, lng):
        police_resp = requests.get(
            POLICE_URL % (lat, lng), timeout=REQUEST_TIMEOUT
        )

        if police_resp.status_code == 404:
            raise forms.ValidationError("No results")

        if not police_resp.ok:
            raise UnexpectedException()

        police = police_resp.json()
        return police['force']

    def get_pcc(self):
        from pages.models import PCCPage

        lat, lng = self._clean_geo()
        police_force = self._get_police_force(lat, lng)

        try:
            return PCCPage.objects.get(pcc_slug=police_force)
        except PCCPage.DoesNotExist:
            pass

        raise forms.ValidationError("No results")

    def clean(self):
        # if errors => skip
        if self.errors:
            return

        try:
            self.cleaned_data['pcc'] = self.get_pcc()
        except (
            UnexpectedException,
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError
        ):
            raise forms.ValidationError(
                "There was an error with your request, please try again."
            )

        return self.cleaned_data
