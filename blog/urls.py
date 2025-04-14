from django.urls import path
from.views import PostListView,PostDetailView
from .import views

urlpatterns = [
    # path("home/", views.home, name = "blog-home"),
    path("", PostListView.as_view(), name = "blog-home"),
    path("post/<int:pk>/",PostDetailView.as_view(),name = "post-details"),
      path("about/", views.about, name = "blog-about"),
]