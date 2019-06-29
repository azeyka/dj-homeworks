from django import forms
from .models import Profile

class SubscribeForm(forms.ModelForm):
  class Meta(object):
    model = Profile
    fields = ()