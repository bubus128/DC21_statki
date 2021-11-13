from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='main'),
    path('form1/', views.vehregister, name='vehregister'),
    path("form2/", views.vehderegister, name="vehderegister"),
    path("form3/", views.form3, name="form3"),
    path("myforms/", views.myforms, name="myforms"),
]
