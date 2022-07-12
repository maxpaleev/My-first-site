from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("author", views.author, name="author"),
    path('contacts', views.contacts, name='contacts'),
    path('class', views.clas, name='class'),

]
