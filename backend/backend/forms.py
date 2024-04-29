from django import forms

from .models import Country,Location

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
