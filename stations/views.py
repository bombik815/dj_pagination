import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    my_dict = dict()
    bus_stations = []

    with open(settings.BUS_STATION_CSV, 'r', encoding="utf-8", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=',')
        for row in reader:
            my_dict = {'Name': row['Name'],
                       'Street': row['Street'],
                       'District': row['District']}
            bus_stations.append(my_dict)

    # Пагинация
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
          'bus_stations': bus_stations,
          'page': page,
    }
    return render(request, 'stations/index.html', context)
