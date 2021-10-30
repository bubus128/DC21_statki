from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('formularz.html', views.formularz, name='formularz'),
]