from django.contrib import admin
from django.urls import path
from example import views
urlpatterns = [
    path("", views.index, name="index"),
    path("", views.index, name='Home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("Students", views.Students, name='Students'),
    path("Faculty", views.Faculty, name='Faculty'),
]