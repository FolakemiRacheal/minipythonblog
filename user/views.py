from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserSignupForm


def signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"account Created Successfully for {username}!")
            return redirect("login")
    else:
        form = UserSignupForm()
    return render(request, "user/signup.html", {"form":form})

