from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class signUpForm(UserCreationForm):
    class Meta:
        model=User
        fields= ('username','email','password1','password2')

    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class':'w-3/4 ms-12 py-4 px-6 rounded-lg'
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Email@example.example',
        'class': 'w-3/4 ms-12 py-4 px-6 rounded-lg'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-3/4 ms-12 py-4 px-6 rounded-lg'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeated Password',
        'class': 'w-3/4 ms-12 py-4 px-6 rounded-lg'
    }))

class logInForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'w-3/4 ms-12 py-4 px-6 rounded-lg'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-3/4 ms-12 py-4 px-6 rounded-lg'
    }))