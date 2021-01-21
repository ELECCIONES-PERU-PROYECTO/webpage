from django.urls import path

from . import views

app_name = 'elecciones'

urlpatterns = [
  path('candidatos', views.candidatos),
]