from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from random import randint
from markdown2 import Markdown
from . import util



class Search(forms.Form):
    title = forms.CharField(label= "", widget=forms.TextInput(
        attrs={"placeholder": "Search Encyclopedia"}))
    

class NewPage(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(
        attrs={"placeholder": "Title"}))
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={"placeholder": "Input Markdown Content"}))

class EditPage(forms.Form):
    content = forms.CharField(label="", widget=forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "search": Search(),
        "entries": util.list_entries()
    })


def wiki(request, title):
    if request.method == "POST":
        editpage = EditPage(request.POST)
        if editpage.is_valid():
            content = editpage.cleaned_data["content"]
            util.save_entry(title, content)
    
    name = "Error"
    for entry in util.list_entries():
        if title.casefold() == entry.casefold(): name = entry

    markdowner = Markdown()
    return render(request, "encyclopedia/wiki.html", {
        "search": Search(),
        "name": name,
        "contents": markdowner.convert(util.get_entry(name))
    })


def search_result(request):
    if request.method == "POST":
        search = Search(request.POST)
        if search.is_valid():
            title = search.cleaned_data["title"]

    if title.casefold() in [x.casefold() for x in util.list_entries()]:
        return redirect("wiki", title)
    
    matches = []
    for entry in [x.casefold() for x in util.list_entries()]:
        if entry.find(title.casefold()) != -1:
            matches.append(entry)
   
    if matches:
        return render(request, "encyclopedia/search_result.html", {
            "search": Search(),
            "title": title,
            "matches": matches
        })
    else: return redirect("wiki", title)


def new(request):
    if request.method == "POST":
        newpage = NewPage(request.POST)
        if newpage.is_valid():
            title = newpage.cleaned_data["title"]
            content = newpage.cleaned_data["content"]
            if title.casefold() in [x.casefold() for x in util.list_entries()]:
                msg = "Entry already exists with the provided title"
                return render(request, "encyclopedia/error.html", {"search": Search(), "msg": msg})
            else: 
                util.save_entry(title, content)
                redirect("new")

    return render(request, "encyclopedia/new.html", {
        "search": Search(),
        "newpage": NewPage()
    })


def edit(request, title):
    editpage = EditPage(initial={"content": util.get_entry(title)})
    return render(request, "encyclopedia/edit.html", {
        "search": Search(),
        "title": title,
        "editpage": editpage
    })


def random(request):
    entries = util.list_entries()
    rnd = randint(0, len(entries) - 1)
    name = entries[rnd]
    
    markdowner = Markdown()
    return render(request, "encyclopedia/wiki.html", {
        "search": Search(),
        "name": name,
        "contents": markdowner.convert(util.get_entry(name))
    })