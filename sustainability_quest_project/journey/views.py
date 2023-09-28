from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Hero
from django.contrib.auth.decorators import login_required
from django.contrib import admin
# from .forms import PostForm

# Create your views here.
@login_required
def index(requests):
    tasks = Post.objects.all()
    print('Hello World!')
    return render(requests, 'index.html', {'tasks':tasks})
    
    

