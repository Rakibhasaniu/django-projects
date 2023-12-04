from django import forms


class contact_form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()