from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
import urllib.parse
import csv


def index(request):
    return redirect(reverse(bus_stations))

def bus_stations(request):
    curr_page = request.GET.get('page') or '1'

    bus_stations = get_bus_stations_dict()
    next_page_url, prev_page_url = get_next_and_prev_urls(str(len(bus_stations)), curr_page)

    context = {
        'bus_stations': bus_stations[int(curr_page)],
        'current_page': curr_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }

    return render_to_response('index.html', context=context)

def get_bus_stations_dict():
    bus_stations = {}
    path = settings.BUS_STATION_CSV

    with open(path, newline='', encoding='cp1251') as file:
        reader = csv.DictReader(file)
        bus_station_num = 0
        page = 1
        bus_stations[page] = []

        for row in reader:
            if bus_station_num == 10:
                bus_station_num = 0
                page += 1
                bus_stations[page] = []

            bus_station_info = {}
            bus_station_info['Name'] = row['Name']
            bus_station_info['Street'] = row['Street']
            bus_station_info['District'] = row['District']
            bus_stations[page].append(bus_station_info)
            bus_station_num += 1

    return bus_stations

def get_next_and_prev_urls(last_page, curr_page):
    next_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': int(curr_page) + 1})
    prev_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': int(curr_page) - 1})
    if curr_page == '1':
        prev_page_url = None
    elif curr_page == last_page:
        next_page_url = None

    return next_page_url, prev_page_url