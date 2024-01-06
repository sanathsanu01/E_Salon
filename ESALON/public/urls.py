from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [                 
    path('',views.index),
    path('login',views.login),
    path('contact',views.contact),
    path('saloonreg',views.saloonreg),
    path('about',views.about)
]