from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import string
import json

with open("data/country-by-languages.json") as f:
    countries_data = json.load(f)


def home(request):
    return render(request, "home.html")


def countries_list(request):
    object_list = []
    for i in countries_data:
        object_list.append(i["country"])
    page_num = request.GET.get('page', 1)
    paginator = Paginator(object_list, 10)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'countries_list.html', {'page_obj': page_obj,
                                                   's': list(string.ascii_uppercase)})


def countries_buc(request, buc):
    return render(request, "countries_buc.html", {'co': countries_data,
                                                  'buc': buc})


def country(request, id):
    return render(request, "country.html", {'co': countries_data,
                                            'id': id})


def lenguages(request):
    object_list = []
    for i in countries_data:
        for j in i['languages']:
            object_list.append(j)
    object_list = list(set(object_list))
    object_list.sort()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(object_list, 20)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "lenguages.html", {'page_obj': page_obj})


def lenguag(request, len):
    return render(request, "lenguag.html", {'co': countries_data,
                                            'len': len})
