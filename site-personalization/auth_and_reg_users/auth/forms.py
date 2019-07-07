from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=20, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(), label='Придумайте пароль')
    password_repeat = forms.CharField(widget=forms.PasswordInput(), label='Подтвердите пароль')

    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_repeat

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')