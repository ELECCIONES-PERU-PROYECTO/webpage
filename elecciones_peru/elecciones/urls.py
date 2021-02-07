from django.urls import path

from . import views

app_name = 'elecciones'
#http://127.0.0.1:8000/elecciones/candidatos/estudios/concluyo_primaria
urlpatterns = [
  path('', views.mainpage),
  #path('candidatos', views.candidatos),
  path('candidatos', views.filterpage),
  path('candidatos/estudios/<str:nivel_academico>', views.test_query),
  path('candidato/hojadevida/<str:dni_hoja_de_vida>/<str:cargo_eleccion_>', views.hojadevida_by_dni),
  path('candidatos/<str:nivel_academico>', views.test_query),
  path('candidatos/<str:nivel_academico>/<str:cargos_previos_order>/<str:orden_cant_sentencia>/<str:orden_cant_sentencia_oblig>/<str:mat_demanda>/<str:no_tiene_val>/<str:orden_cant_ingreso>/<str:orden_cant_inmueble>/<str:orden_valor_inmueble>/<str:orden_cant_mueble>/<str:orden_valor_mueble>/<str:orden_renuncias>/<str:rango_edad_val>/<str:nac_per_si>/<str:nac_per_no>/<str:departamento_nacimiento>/<str:cargo_postula>/<str:org_politica>/<str:dist_electoral>/<str:tipo_candidato_>', views.filter_function),
  path('candidatos/<str:filtro_id>/<str:info_extra>/<str:orden>', views.filter_function_orga)
]
