from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader


def index(request):
    return redirect(reverse('bus_stations'))


with open('/home/rahmidin/PycharmProjects/pagination/data-398-2018-08-30.csv', 'r') as file:
    reader = DictReader(file)
    stations = []
    for item in reader:
        stations.append(item)


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    paginato = Paginator(stations, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginato.get_page(page_number)

    context = {
        'bus_stations': stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
