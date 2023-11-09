from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from posts.models import Post
from .models import *
from django.contrib.auth import login as auth_login
from .forms import *

# ...

def login_view(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        return render(request, "post_list.html", {"posts": posts})
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error": "Invalid credentials"}
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect('/')

    return render(request, "accounts/login.html", {})

    #     else:
    #         # Authentication was successful, log the user in
    #         login(request, user)
    #     #     # You can redirect the user to another page or return a success response here
    #     #     return redirect("post_list", {"posts":posts})  # Replace "home" with the name of your home page URL pattern
    # else:
    #     # Handle GET request by rendering the login form
    #     # return render(request, "accounts/login.html", {})
    # return render(request, "accounts/logout.html", {})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    return render(request, "accounts/logout.html", {})


def register_view(request):
    if request.method == "POST":
        logout(request)
    return render(request, "accounts/logout.html", {})

     
def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'signup.html', {"form":form})

