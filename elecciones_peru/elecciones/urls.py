from django.urls import path
from . import views

app_name = 'elecciones'
urlpatterns = [
  path('', views.mainpage, name="mainpage"),
  path('analisis-graficos', views.analisisGraficos, name="analisisGraficos"),
  # path('busqueda', views.candidatos, name="candidatos"),
  path('candidato/hojadevida/<str:dni_hoja_de_vida>/<str:cargo_postula_dato>', views.hojadevida_by_dni, name="hojadevida_by_dni"),
  path('busqueda', views.filter_function, name="candidatos"),
  path('busqueda/<str:filtro_id>/<str:info_extra>/<str:orden>', views.filter_function_orga, name="filter_function_orga"),
  # path('subir/',views.subir_data,name='subir_data'),
  # path('eliminar/', views.eliminar_data, name='eliminar_data'),
  # path('correjir', views.corregir_data, name='correjir'),
  path('test', views.test, name='test')
]
