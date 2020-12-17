from os import name
from home.views import index
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name= 'home'),
    path('home',views.index, name= 'home'),
    path('about',views.about, name='about'),
    path('Category',views.Category, name='services'),
    path('Books',views.Books, name='services'),
    path('Contact',views.contact, name='contact'),
    path('signup',views.signup, name='signup')
]
