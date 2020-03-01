from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:slug>',views.blogpost,name="blogpost"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact")
]
