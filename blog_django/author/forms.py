from django import forms
from .models import Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model= Author
#         fields = '__all__'

class RegistrationForm(UserCreationForm):
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']