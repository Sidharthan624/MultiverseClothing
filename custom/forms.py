# forms.py

from django import forms
from .models import Design


class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ['design','size','color','print','fit']

