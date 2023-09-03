from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control mb-4'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'}))