from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Profile import views

urlpatterns = [
    #Hola soy ricardo
    re_path(r'profile_list/$', views.ProfileList.as_view()),
    re_path(r'genero_list/$', views.GeneroList.as_view()),
    re_path(r'ocupacion_list/$', views.OcupacionList.as_view()),
    re_path(r'estado_list/$', views.EstadoList.as_view()),
    re_path(r'ciudad_list/$', views.CiudadList.as_view()),
    re_path(r'estadocivil_list/$', views.EstadoCivilList.as_view())
]