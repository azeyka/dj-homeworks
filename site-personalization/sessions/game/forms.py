from django import forms

class SetNumberForm(forms.Form):
  number = forms.IntegerField(label='Загадайте число:')

class CheckNumberForm(forms.Form):
  try_number = forms.IntegerField(label='Попытайтесь отгадать')
