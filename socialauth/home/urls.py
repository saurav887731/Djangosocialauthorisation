from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("about", views.about, name='about'),
    path("login",views.loginuser,name='login'),
    path("logout",views.logoutuser,name='logout'),
   path("", views.index, name='home'),
   path("services", views.services, name='services'),
   path("contacts", views.contacts,name='contacts'),
   path("signuser",views.signuser,name='signuser')
]
