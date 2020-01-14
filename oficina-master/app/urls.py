from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.index),
    path('iniciosesion/', views.iniciosesion),
    path('cerrarsesion/', views.cerrarsesion),
    path('calendar/', views.calendar),
    path('registro/', views.registro),
    path('eliminar/', views.eliminar),
    path('lista/', views.lista),
    path('upload/', views.upload),
    path('jefe/', views.jefe),
    path('docente/', views.docente),
    path('edit/', views.edit),
    
]
