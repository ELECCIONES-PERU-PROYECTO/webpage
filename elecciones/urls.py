from django.urls import path
from . import views

app_name = 'elecciones'
urlpatterns = [
  path('', views.mainpage, name="mainpage"),
  path('analisis-graficos', views.analisisGraficos, name="analisisGraficos"),
  path('candidato/hojadevida/<str:dni_hoja_de_vida>/<str:cargo_postula_dato>', views.hojadevida_by_dni, name="hojadevida_by_dni"),
  path('inteligencia-articial',views.iaDisplay, name="iaDisplay"),
  path('nosotros', views.nosotros, name="nosotros"),
  path('busqueda', views.filter_function, name="filter_function")
]
