from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name='wiki'),
    path("search_result/", views.search_result, name='search_result'),
    path("new/", views.new, name="new"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random", views.random, name="random")
]
