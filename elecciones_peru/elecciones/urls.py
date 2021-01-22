from django.urls import path

from . import views

app_name = 'elecciones'

urlpatterns = [
  path('candidatos', views.candidatos),
  path('candidatos/estudios/<str:niv_acad>', views.grado_estudios),
  path('candidato/dni/<str:dni>', views.candidato_by_dni),
]