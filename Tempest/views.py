from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'map.html')

def list(request):
    return render(request, 'list.html')

def about(request):
    return render(request, 'about.html')

def info(request):

    '''import requests'''
    headers = {
        'api_key': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJndWlsbGVqamhAZ21haWwuY29tIiwianRpIjoiNmZjYjM4OTYtMTdlNi00YzMyLTk0ZTYtZDVjMDA1MzY2NzFiIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MTg2NzI4NTEsInVzZXJJZCI6IjZmY2IzODk2LTE3ZTYtNGMzMi05NGU2LWQ1YzAwNTM2NjcxYiIsInJvbGUiOiIifQ.ByKmQAjWDf5lt854PRA8m1hXsdtgiwIwLPNEF6TTNK8'
    }

    url = 'https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/28001'

    respuesta = requests.get(url, headers=headers)
    respuesta = respuesta.json()

    datos = requests.get(respuesta["datos"]).json()

    # Todos los datos
    # print(datos)

    # Prediccion
    # print(datos[0]["prediccion"]["dia"][0])

    # Fecha de la prediccion - Cambiar el 1 para vanzar de dia
    #print(datos[0]["prediccion"]["dia"][1]["fecha"])

    #print(datos[0]["prediccion"]["dia"][1]["probPrecipitacion"])



    diccionario = {'dato1': datos[0]["prediccion"]["dia"][1]["fecha"],
                   'dato2': datos[0]["prediccion"]["dia"][1]["probPrecipitacion"]}
    return render(request, 'info.html', context=diccionario)

    #return render(request, 'info.html')