from django.db import models

from django.db import models

class Station(models.Model):
  latitude = models.FloatField(verbose_name='Широта')
  longitude = models.FloatField(verbose_name='Долгота')
  routes = models.ManyToManyField('Route', related_name="stations")
  name = models.CharField(max_length=50, verbose_name='Название станции')

  def __str__(self):
    return self.name

class Route(models.Model):
  name = models.CharField(max_length=10, verbose_name='Название маршрута')

  def __str__(self):
    return self.name
