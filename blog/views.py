from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    posts = Post.objects.all()

    content = {
        "posts":posts
    }

    return render(request,'blog/index.html',content)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug)[0]
    slugpost={
        'post':post
    }
    return render(request,'blog/post.html',slugpost)

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        textarea = request.POST['textarea']

        contactt = Contact(name=name,email=email,tellme=textarea)
        contactt.save()
    return render(request,'blog/contact.html')