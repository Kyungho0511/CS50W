from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<str:title>", views.listing, name="listing"),
    path("closed_listing", views.closed_listing, name="closed_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories_view, name="categories"),
    path("categories/<str:category>", views.categories_listing, name="categories_listing")
]
