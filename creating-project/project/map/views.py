from django.shortcuts import render
from map.models import Route, Station


def station_view(request):
  context = {}
  routes = Route.objects.all()
  context['routes'] = routes
  context['center'] = {'x': 55.76, 'y': 37.64}

  route = request.GET.get('route')
  if route:
    context['route'] = Route.objects.get(name=route)
    stations = Station.objects.filter(routes__name=route).order_by('latitude')
    x = (stations.first().latitude + stations.last().latitude)/2
    stations = stations.order_by('longitude')
    y = (stations.first().longitude + stations.last().longitude) / 2
    context['stations'] = stations
    context['center'] = {'x': x, 'y': y}

  return render(
    request,
    'stations.html',
    context
  )