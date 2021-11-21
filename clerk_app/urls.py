from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='main'),
    path('myissues/', views.myissues, name='myissues'),
    path("form/<str:form_type>/<int:form_id>", views.singleissue, name="singleissue")
]
