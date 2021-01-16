from django import forms
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label = 'username')
    nickname = forms.CharField(label = 'nickname')
    password = forms.CharField(label = 'password')
    re_password = forms.CharField(label = 're_password')
    email = forms.EmailField(label = 'email')

    class Meta:
        model = User
        fields = ("username", "nickname", 'email')
