from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from Inicio.models import Categoria
from .serializers import CategoriaSerializer
from Inicio.models import Producto
from .serializers import ProductoSerializer

@api_view(['GET'])
def lista_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)
