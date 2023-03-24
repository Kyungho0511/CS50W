from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auctions, AuctionsForm


def index(request):

    # Get all objects from Acutions
    auctions = Auctions.objects.all()
    return render(request, "auctions/index.html", {
        "auctions": auctions
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    

def create_listing(request):
        if request.method == "POST":

            # Add an item to the auction list
            auctions_form = AuctionsForm(request.POST)
            if auctions_form.is_valid():
                auctions_form.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, 'An item has not been added.')
        else:
            return render(request, "auctions/create_listing.html", {
                "auctions_form": AuctionsForm()
            })
        

def listing(request, title):
    if request.method == "POST":

        # Add, remove watchlist
        if request.POST["watchlist"] == "add":
            request.session["watchlist"] += [title]
        elif request.POST["watchlist"] == "remove":
            request.session["watchlist"].remove(title)
            request.session.modified = True
        return HttpResponseRedirect(reverse('listing', args=(title,)))
    
    # Check if an item is already in watchlist
    if "watchlist" not in request.session:
        request.session["watchlist"] = []
    if title in request.session["watchlist"]:
        watchlist = True
    else : 
        watchlist = False
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    # Check if the item is listed by the user
    username = Auctions.objects.get(title=title).username
    if request.user.username == username:
        host = True
    else:
        host = False

    item = Auctions.objects.get(title=title)
    return render(request, "auctions/listing.html", {
        "item": item,
        "watchlist": watchlist,
        "logged_in": logged_in,
        "host": host
    })
    