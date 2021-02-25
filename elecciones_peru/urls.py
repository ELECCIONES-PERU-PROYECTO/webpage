from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from .elecciones import urls as urls_
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls_, namespace='elecciones'))
]

if settings.DEBUG_TOOLBAR:
    import debug_toolbar  # pylint: disable=import-outside-toplevel

    urlpatterns = [path("debug/", include(debug_toolbar.urls)),] + urlpatterns