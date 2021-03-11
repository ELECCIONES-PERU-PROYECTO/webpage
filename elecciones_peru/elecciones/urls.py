from django.urls import path
from . import views

app_name = 'elecciones'
urlpatterns = [
  path('', views.mainpage, name="mainpage"),
  path('analisis-graficos', views.analisisGraficos, name="analisisGraficos"),
  path('candidato/hojadevida/<str:dni_hoja_de_vida>/<str:cargo_postula_dato>', views.hojadevida_by_dni, name="hojadevida_by_dni"),
  path('busqueda', views.filter_function, name="candidatos"),
  # path('subir/',views.subir_data,name='subir_data'),
  # path('eliminar/', views.eliminar_data, name='eliminar_data'),
  # path('correjir', views.corregir_data, name='correjir'),
  # path('test', views.test, name='test')
]
