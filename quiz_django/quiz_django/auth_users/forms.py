from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class AuthForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Your name', max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')