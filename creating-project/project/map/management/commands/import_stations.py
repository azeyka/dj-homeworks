import csv


from django.core.management.base import BaseCommand
from map.models import Route, Station

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', 'r') as file:
          station_reader = csv.reader(file, delimiter=';')
          # пропускаем заголовок
          next(station_reader)

          for line in station_reader:
            station = Station.objects.create(
              latitude=float(line[3]),
              longitude=float(line[2]),
              name=line[1]
            )

            for route_name in line[7].split('; '):
              try:
                route = Route.objects.get(name=route_name)
              except Route.DoesNotExist:
                route = Route.objects.create(name=route_name)

              station.routes.add(route)
