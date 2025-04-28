from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .import models


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2', "avatar")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class AvatarForm(forms.ModelForm):
    class Meta:
        model = models.Avatar
        fields = ['image']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    # password = forms.CharField(
    #     label='Nueva contraseña',
    #     widget=forms.PasswordInput,
    #     required=False,
    #     help_text='Dejar en blanco si no quieres cambiarla.'
    # )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        # new_password = self.cleaned_data.get('password')
        # if new_password:
        #     user.set_password(new_password)
        if commit:
            user.save()
        return user
