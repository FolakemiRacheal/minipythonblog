from django.urls import path
from.views import PostListView,PostDetailView, PostCreateView, PostupdateView, PostDeleteView
from .import views

urlpatterns = [
     path("home/", views.home, name = "blog-home"),
    path("", PostListView.as_view(), name = "blog-home"),
    path("post/<int:pk>/",PostDetailView.as_view(),name = "post-details"),
    path("post/new/", PostCreateView.as_view(), name = "post_create"),
     path("post/<int:pk>/update", PostupdateView.as_view(), name = "post_update"),
     path("post/<int:pk>/delete/",PostDeleteView.as_view(),name = "post-delete"),
     
      path("about/", views.about, name = "blog-about"),
]