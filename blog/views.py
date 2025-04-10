from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {
    "author" : "folake Racheal",
    "title" : "learning Django",
    "content" : "Django from scriptDesk",
    "date_posted": "March 28, 2025"
    },
     {
    "author" : "Olusoji micheal",
    "title" : "line manager",
    "content" : "Giver of django tutorial",
    "date_posted": "March 26, 2025"
    }


]

def home(request):
    context = {
        "posts": posts
     }
    # return HttpResponse("<h1>Blog home</h1>")
    return render(request, "blog/home.html",context)

def about(request):
    #   return HttpResponse("<h2>about</h2>")
    return render(request, "blog/about.html", {"title": "about"})

#blog -> templates -> blog -> templates -> templates.html
#web app part 3 Templates

