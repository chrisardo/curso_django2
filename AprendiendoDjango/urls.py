"""
URL configuration for AprendiendoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from AprendiendoDjango.views import bienvenida, bienvenidaRojo

# Importamos la vista 'bienvenida' de la app 'bienvenida'.

from AprendiendoDjango.views import categoriaEdad, obtenerMomentoActual
from AprendiendoDjango.views import contenidoHtml
from AprendiendoDjango.views import miPrimeraPlantilla, plantillaParamtros
from AprendiendoDjango.views import palntillasCargados
from AprendiendoDjango.views import palntillaShortcut, plantillaHija, plantillaHija2

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "bienvenida/", bienvenida
    ),  # Agregamos la ruta de la app 'bienvenida' a la lista de rutas.
    path(
        "bienvenidaRojo/", bienvenidaRojo
    ),  # Agregamos la ruta de la app 'bienvenida' a la lista de rutas.
    # path("edad/<int:edad>/", categoriaEdad),
    path("obtenerMomentoActual/", obtenerMomentoActual),
    path("contenidoHtml/<str:nombre>/<int:edad>/", contenidoHtml),
    path("miPrimeraPlantilla/", miPrimeraPlantilla),
    path("plantillaParamtros/", plantillaParamtros),
    path("palntillasCargados/", palntillasCargados),
    path("palntillaShortcut/", palntillaShortcut),
    path("plantillaHija/", plantillaHija),
    path("plantillaHija2/", plantillaHija2),
]
