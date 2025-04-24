from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ( 
ListView, 
DetailView,
CreateView,
UpdateView,
DeleteView
)
# Create your views here.

posts = [
    {
    "author": "folake",
    "title":"blog 1",
    "content":"update"
    "date_posted"
    },
    {
    "author": "folake",
    "title":"blog 1",
    "content":"update"
    "date_posted"
    }
]

def home(request):
    context = {
        'post':posts
    #     "posts": Post.objects.all
    }
    # return HttpResponse("<h1>Blog home</h1>")
    return render(request, "blog/home.html",context)

# help us get all post
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-dated_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostupdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/" # where to be redirect to after the delete view is a success

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    #   return HttpResponse("<h2>about</h2>")
    return render(request, "blog/about.html", {"title": "about"})

#blog -> templates -> blog -> templates -> templates.html
#web app part 3 Templates


