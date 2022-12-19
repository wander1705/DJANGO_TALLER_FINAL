from django.shortcuts import render, redirect
from persona_APP.models import Proyecto, Institucion
from persona_APP.forms import FormProyecto
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ProyectosSerializer, InstitucionSerializer
from rest_framework.views import APIView
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'index.html')

def listarinscripcion(request):
    pro = Proyecto.objects.all()
    data = {'proyecto': pro}
    return render(request, 'listarinscripcion.html', data)

def agregarinscripcion(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarinscripcion.html', data)

def eliminarinscripcion(request, id):
    pro = Proyecto.objects.get(id = id)
    pro.delete()
    return redirect('/inscripciones')

def actualizarinscripcion(request, id):
    pro = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=pro)
    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarinscripcion.html', data)



def verinscripcionDb(request):
    Inscritos = Proyecto.objects.all()
    data = {'inscritos' : list(Inscritos.values('id', 'nombre', 'telefono', 'fechainscripcion', 'institucion', 'horainscripcion', 'estado', 'observacion'))}

    return JsonResponse(data)

#Funcion based

@api_view(['GET', 'POST'])
def inscripcion_list(request):
    if request.method == 'GET':
        estu = Institucion.objects.all()
        serial = InstitucionSerializer(estu, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def inscripcion_detalle(request, pk):
    try:
        estu = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(estu)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Class

class Listarinscritos(APIView):

    def get(self, request):
        estu = Proyecto.objects.all()
        serial = ProyectosSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = ProyectosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Detalleinscrito(APIView):

    def get_object(self, pk):
        try:
            return Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = ProyectosSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = ProyectosSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)