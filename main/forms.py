from django import forms

from .models import Email, Contact


class InputForm(forms.Form):
    contact = forms.CharField(required=True)

    # doing EmailInput makes the field not show up on the webpage
    email = forms.EmailField(required=True)
