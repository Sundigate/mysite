from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('excursions', views.excursions, name='excursions'),
    path('contacts', views.contacts, name='contacts'),
    path('galery', views.galery, name='galery'),
]