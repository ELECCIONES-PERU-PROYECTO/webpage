from django.urls import path
from . import views

app_name = 'elecciones'
urlpatterns = [
  path('', views.mainpage, name="mainpage"),
  path('analisis-graficos', views.analisisGraficos, name="analisisGraficos"),
  path('busqueda', views.filter_function, name="filter_function"),
  path('candidato/hojadevida/<str:dni_hoja_de_vida>/<str:cargo_postula_dato>', views.hojadevida_by_dni, name="hojadevida_by_dni"),
  #path('subir/',views.subir_data,name='subir_data'),
  #path('eliminar/', views.eliminar_data, name='eliminar_data'),
  #path('correjir', views.corregir_data, name='correjir')
]

handler404 = 'elecciones.views.error_404'
handler500 = 'elecciones.views.error_500'
handler403 = 'elecciones.views.error_403'
handler400 = 'elecciones.views.error_400'
