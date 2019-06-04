from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator

import urllib.parse
import csv


def index(request):
    return redirect(reverse(bus_stations))

def bus_stations(request):
    curr_page = request.GET.get('page') or 1

    with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as file:
        reader = csv.DictReader(file)
        paginator = Paginator(list(reader), 10)

    next_page_url, prev_page_url = get_next_and_prev_urls(paginator.num_pages, int(curr_page))

    bus_stations = paginator.get_page(curr_page)

    context = {
        'bus_stations': bus_stations,
        'current_page': curr_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }

    return render_to_response('index.html', context=context)

def get_next_and_prev_urls(last_page, curr_page):
    next_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': curr_page + 1})
    prev_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': curr_page - 1})
    if curr_page == 1:
        prev_page_url = None
    elif curr_page == last_page:
        next_page_url = None

    return next_page_url, prev_page_url