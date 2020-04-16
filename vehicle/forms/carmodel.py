from django import forms

from vehicle.models import CarModel

class CarModelForm(forms.ModelForm):

    class Meta:
        model = CarModel
        fields = ("brand", "code", "desc")