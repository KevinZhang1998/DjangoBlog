from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



# 原表格没有email字段，需要重新编写一个表格，通过继承 UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        # Give your model metadata by using an inner class Meta,
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
