from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets,ModelForm
from django import forms
from .models import Profile

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
