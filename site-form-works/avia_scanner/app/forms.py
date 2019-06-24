from django import forms

from .widgets import AjaxInputWidget, CalendarWidget
from .models import City


class SearchTicket(forms.Form):
    departure = forms.CharField(label='Город отправления',
                                widget=AjaxInputWidget(url='api/city_ajax', attrs={'class': 'inline right-margin'}))
    arrival = forms.ModelChoiceField(label='Город прибывания', queryset=City.objects.all())
    date = forms.DateField(label='Дата вылета', widget=CalendarWidget())

