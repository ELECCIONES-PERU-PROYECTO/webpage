from django.urls import path
from . import views

app_name = 'elecciones'
urlpatterns = [
  path('', views.mainpage, name="mainpage"),
  path('analisis-graficos', views.analisisGraficos, name="analisisGraficos"),
  path('analisis-graficos-presi', views.analisisGraficosPresi, name='analisisGraficosPresi'),
  path('', views.candidatos, name='candidatos'),
  path('candidato/hojadevida/<str:dni_hoja_de_vida>/<str:cargo_postula_dato>', views.hojadevida_by_dni, name="hojadevida_by_dni"),
  path('inteligencia-articial',views.iaDisplay, name="iaDisplay"),
  path('busqueda', views.filter_function, name="filter_function")
]
