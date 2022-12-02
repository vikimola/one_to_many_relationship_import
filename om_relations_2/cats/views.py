from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from cats.models import Cat, Breed


def home(request):
    return HttpResponse("Yo")


class CatList(ListView):
    model = Cat
    template_name = "cats/templates/cat_list.html"


class BreedList(ListView):
    model = Breed
    template_name = "cats/templates/breed_list.html"


class CatItem(DetailView):
    model = Cat
    template_name = "cats/templates/cat_detail.html"

