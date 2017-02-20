# try/views.py

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Post


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def nothing_here(request):
    return HttpResponse("Nothing Here!")

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})


