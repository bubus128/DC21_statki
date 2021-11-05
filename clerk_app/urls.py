from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='main'),
    path('myissues/', views.myissues, name='myissues'),
]
