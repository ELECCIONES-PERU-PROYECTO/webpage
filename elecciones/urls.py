from django.urls import path
from . import views

app_name = 'elecciones'
urlpatterns = [
  path('', views.mainpage, name="mainpage"),
  path('analisis-graficos', views.analisisGraficos, name="analisisGraficos"),
  path('busqueda', views.candidatos, name="candidatos"),
  path('candidato/hojadevida/<str:dni_hoja_de_vida>/<str:cargo_postula_dato>', views.hojadevida_by_dni, name="hojadevida_by_dni"),
  path('busqueda/<str:nivel_academico>/<str:cargos_previos_order>/<str:orden_cant_sentencia>/<str:orden_cant_sentencia_oblig>/<str:mat_demanda>/<str:no_tiene_val>/<str:orden_cant_ingreso>/<str:orden_cant_inmueble>/<str:orden_valor_inmueble>/<str:orden_cant_mueble>/<str:orden_valor_mueble>/<str:orden_renuncias>/<str:rango_edad_val>/<str:nac_per_si>/<str:nac_per_no>/<str:departamento_nacimiento>/<str:cargo_postula>/<str:org_politica>/<str:dist_electoral>/<str:tipo_candidato_>', views.filter_function, name="filter_function"),
  path('busqueda/<str:filtro_id>/<str:info_extra>/<str:orden>', views.filter_function_orga, name="filter_function_orga")
  #path('subir/',views.subir_data,name='subir_data'),
  #path('eliminar/', views.eliminar_data, name='eliminar_data'),
  #path('correjir', views.corregir_data, name='correjir')
]
