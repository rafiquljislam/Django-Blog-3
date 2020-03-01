from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    tellme = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
