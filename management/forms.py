from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='', widget= forms.TextInput(attrs={'placeholder': 'Username', 'class': 'mb-4'}))
    email = forms.EmailField(max_length=50, label='', widget= forms.EmailInput(attrs={'placeholder' : 'Email', 'class': 'mb-4'}))
    password1 = forms.CharField(max_length=50, label='', widget= forms.TextInput(attrs={'placeholder': 'Password', 'class': 'mb-4', 'type':'password'}))
    password2 = forms.CharField(max_length=50, label='', widget= forms.TextInput(attrs={'placeholder': 'Confirm password', 'class': 'mb-4', 'type':'password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']





