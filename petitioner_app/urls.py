from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='main'),
    path('form1/', views.vehregister, name='vehregister'),
    path("form2/", views.vehderegister, name="vehderegister"),
    path("form3/", views.vehreregister, name="vehreregister"),
    path("myforms/", views.myforms, name="myforms"),
    path("form/<str:form_type>/<int:form_id>", views.singleform, name="singleform")
]
