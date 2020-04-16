from django import forms

from vehicle.models import CarBrand

class CarBrandForm(forms.ModelForm):

    class Meta:
        model = CarBrand
        fields = ("code", "desc")