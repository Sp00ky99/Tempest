from django.shortcuts import render
from django.http import HttpResponse
import requests
from BaseMunicipios.models import municipios

def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'map.html')

def list(request):
    '''query = request.GET.get('name')
    message = "El codigo es {}".format(query)
    template = "list.html"
    '''
    context = {
        #'message': message,
        'municipios': municipios.objects.all().order_by('nombre')
    }
    print(context)
    return render(request, 'list.html', context)

def about(request):
    return render(request, 'about.html')

def info(request):
    query = request.GET.get('name')
    message = "El codigo es {}".format(query)
    template = "info.html"
    headers = {
        'api_key': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJndWlsbGVqamhAZ21haWwuY29tIiwianRpIjoiNmZjYjM4OTYtMTdlNi00YzMyLTk0ZTYtZDVjMDA1MzY2NzFiIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MTg2NzI4NTEsInVzZXJJZCI6IjZmY2IzODk2LTE3ZTYtNGMzMi05NGU2LWQ1YzAwNTM2NjcxYiIsInJvbGUiOiIifQ.ByKmQAjWDf5lt854PRA8m1hXsdtgiwIwLPNEF6TTNK8'
    }



    url = 'https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{}'.format(query)
    respuesta = requests.get(url, headers=headers)
    respuesta = respuesta.json()
    datos = requests.get(respuesta["datos"]).json()

    diccionario = {'Nombre': datos[0]["nombre"],
                   'Temperatura': datos[0]["prediccion"]["dia"][0]["temperatura"]}





    context = {
        'message': message,
        'datos': datos,
        'datos': datos,
        'diccionario': diccionario,


    }

    return render(request, template, context)


# Todos los datos
    #print(datos)

    # Prediccion
    #print(datos[0]["prediccion"]["dia"][0])

    # Fecha de la prediccion - Cambiar el 1 para vanzar de dia
    #print(datos[0]["prediccion"]["dia"][3]["fecha"])

    #print(datos[0]["prediccion"]["dia"][1]["probPrecipitacion"])

    #diccionario = {'dato1': datos[0]["prediccion"]["dia"][1]["fecha"],
    #               'dato2': datos[0]["prediccion"]["dia"][1]["probPrecipitacion"]}
    #return render(request, 'info.html', context=diccionario)