from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='main'),
    path('form1/', views.vehregister, name='vehregister'),
    path("form2/", views.form2, name="form2"),
    path("form3/", views.form3, name="form3"),
    path("myforms/", views.myforms, name="myforms"),
    path("form/<int:form_id>", views.singleform, name="singleform")
]
