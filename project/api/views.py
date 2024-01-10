from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSer, CategoriesSer
from .models import Products, Categories
from rest_framework.viewsets import ModelViewSet

# class ProductView(ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductSer

@api_view(['GET'])
def productGet(request):
    products = ProductSer()
    serializer = ProductSer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productGet(request, pk):
    products = Products.objects.get(pk=pk)
    serializer = ProductSer(products)
    return Response(serializer.data)

@api_view(['POST'])
def productApp(request, pk):
    serializer = ProductSer(data=request.data)
    if serializer.is_valid():
        serializer.save
    return Response(serializer.data)