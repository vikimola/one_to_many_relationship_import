from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cats", views.CatList.as_view(), name="cat_list"),
    path("cat/<int:pk>", views.CatItem.as_view(), name="cat"),
    path("breeds", views.BreedList.as_view(), name="breed_list"),
]
