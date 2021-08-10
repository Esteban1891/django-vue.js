from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from apps.facturaxion.models import Factura
from apps.facturaxion.serializers import FacturaSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def facturaxion_create(request):
    if request.method == 'POST':
        factura_datos = JSONParser().parse(request)
        facserializers = FacturaSerializer(data=factura_datos)
        if facserializers.is_valid():
            facserializers.save()
    return JsonResponse(facserializers.data, safe=False)
# Crear nueva factura.


@api_view(['GET'])
def facturaxion_list(request):
    if request.method == 'GET':
        facturas = Factura.objects.all()
    facserializers = FacturaSerializer(facturas, many=True)
    return JsonResponse(facserializers.data, safe=False)
# Consultar facturas.




    
        
