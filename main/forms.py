from django import forms

# from .models import Email, Contact, Message


class InputForm(forms.Form):
    name = forms.CharField(required=True)

    # doing EmailInput makes the field not show up on the webpage
    email = forms.EmailField(required=True)

    message = forms.CharField(widget=forms.Textarea)
