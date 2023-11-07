# appname/forms.py
from django import forms
from .models import FlightValidation

class FlightValidationForm(forms.Form):
    textbox_data = forms.CharField(max_length=200)
