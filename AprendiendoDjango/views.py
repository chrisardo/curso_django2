from django.http import HttpResponse
from datetime import datetime
from django.template import (
    Template,
    Context,
)  # Importamos la clase 'Template' y 'Context' de la libreria 'django.template'.
from django.template import (
    loader,
)  # Importamos la clase 'loader' de la libreria 'django.template'.
from django.template.loader import (
    get_template,
)  # Importamos la clase 'loader' de la libreria 'django.template'.
from django.shortcuts import render

# Request: Para realizar peticionees.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.


# Esto es una vista
def bienvenida(request):  # Pasamos un objeto de tipo request como primer argumento.
    return HttpResponse("Hola, Aprendiendo Django")


def bienvenidaRojo(request):
    return HttpResponse("<p style='color:red'>Hola, Aprendiendo Django</p>")


def categoriaEdad(request, edad):
    if edad < 18:
        if edad >= 60:
            categoria = "Tercera Edad"
        else:
            categoria = "Adltez"
    else:
        if edad >= 10:
            categoria = "Infancia"
        else:
            categoria = "Adolescencia"
    resultado = "<h1>Categoria de la edad: %s</h1>" % categoria
    return HttpResponse(resultado)


def obtenerMomentoActual(request):
    # respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.now())
    respuesta = "<h1>Momento actual: {0}</h1>".format(
        datetime.now().strftime("%A %d/%m/%Y %H:%M:%S")
    )
    return HttpResponse(respuesta)


def contenidoHtml(request, nombre, edad):
    contenido = """
    <html>
        <head>
            <title>Contenido HTML</title>
        </head>
        <body>
            <h1>Contenido HTML</h1>
            <p>Nombre: %s</p>
            <p>Edad: %s</p>
        </body>
    </html>
    """ % (
        nombre,
        edad,
    )
    return HttpResponse(contenido)


def miPrimeraPlantilla(request):
    # Abrimos el documento- que contiene a la plantilla:
    plantillaExterna = open("AprendiendoDjango/Plantillas/primeraPlantilla.html")
    # Cargar el docuemtno en una variable tipo 'Template'
    template = Template(plantillaExterna.read())
    # Cerrar el documento externo que hemos abierto.
    plantillaExterna.close()
    # Crear un contexto para la plantilla.
    contexto = (
        Context()
    )  # Permite indicar que varibles o atributos va utilizar la palntilla, es como un contenedor
    # Renderizar la plantilla con el contexto, devolver como un objeto http.
    docuemntoRenderizado = template.render(contexto)
    # Retornar el documento renderizado.
    return HttpResponse(docuemntoRenderizado)


def plantillaParamtros(request):
    """
    Comentario:
    Esta vista permite renderizar una plantilla que recibe parametros.
    """
    nombre = "Chrisardo"
    fechaActual = datetime.now()
    lenguajes = ["Python", "Java", "C#", "JavaScript", "PHP"]
    # Abrimos el documento- que contiene a la plantilla:
    plantillaExterna = open("AprendiendoDjango/Plantillas/plantillaParametros.html")
    # Cargar el docuemtno en una variable tipo 'Template'
    template = Template(plantillaExterna.read())
    # Cerrar el documento externo que hemos abierto.
    plantillaExterna.close()
    # Crear un contexto para la plantilla.
    contexto = Context(
        {
            "nombrePlantilla": nombre,
            "fechaActualPlantilla": fechaActual,
            "lenguajes": lenguajes,
        }
    )  # Permite indicar que varibles o atributos va utilizar la palntilla, es como un contenedor
    # Renderizar la plantilla con el contexto, devolver como un objeto http.
    docuemntoRenderizado = template.render(contexto)
    # Retornar el documento renderizado.
    return HttpResponse(docuemntoRenderizado)


def palntillasCargados(request):
    nombre = "Chrisardo"
    fechaActual = datetime.now()
    lenguajes = ["Python", "Java", "C#", "JavaScript", "PHP", "Kotlin"]
    # Especificando la carpeta donde se encuentran las plantilla y creamos una variable que la almacena:
    # plantillaExternas = loader.get_template("plantillaParametros.html")
    plantillaExternas = get_template("plantillaParametros.html")
    # Renderizar el documento a retornar:
    documento = plantillaExternas.render(
        {
            "nombrePlantilla": nombre,
            "fechaActualPlantilla": fechaActual,
            "lenguajes": lenguajes,
        }
    )
    return HttpResponse(documento)


def palntillaShortcut(request):  # Atajo para renderizar una plantilla
    nombre = "Chrisardo"
    fechaActual = datetime.now()
    lenguajes = ["Python", "Java", "Swift", "JavaScript", "PHP", "Kotlin"]

    return render(
        request,
        "plantillaParametros.html",
        {
            "nombrePlantilla": nombre,
            "fechaActualPlantilla": fechaActual,
            "lenguajes": lenguajes,
        },
    )


def plantillaHija(request):
    return render(request, "plantillaHija1.html", {"nombre": "Chrisardo"})


def plantillaHija2(request):
    return render(request, "plantillaHija2.html", {"nombre": "Chrisardo"})
