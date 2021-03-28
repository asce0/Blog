from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, 'blog/index.html', context)


def log_in(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           return redirect('index')

    return render(request, 'blog/login.html')


def log_out(request):
    logout(request)
    return render(request, 'blog/index.html')


def register(request):
    return render(request, 'blog/register.html')


def register_form(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(
        username=username, password=password, email=email)
    user.save()
    return render(request, 'blog/login.html')


def post_creation(request):
    if not request.user.is_authenticated:
        return redirect('log_in')
    if request.method == "POST":
        post = Post()
        post.title = request.POST['title']
        post.description = request.POST['content']
        post.author = request.user
        post.save()
        return redirect('index')
    return render(request, 'blog/create_post.html')

