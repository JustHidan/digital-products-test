from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, Category, File
from products.serializers import ProductSerializer, CategorySerializer, FileSerializer


# Create your views here.
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True,context= {'request':request} )
        return Response(serializer.data)

class ProductDetailView(APIView):
    def get(self,request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response( "file ni ", status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context= {'request':request})
        return Response(serializer.data)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True,context= {'request':request})
        return Response(serializer.data)

class CategoryDetailView(APIView):
    def get(self,request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response( "file ni ", status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, context= {'request':request})
        return Response(serializer.data)

class FileListView(APIView):
    def get(self, request,p_id):
        try:
            files = File.objects.filter(product_id=p_id)
        except File.DoesNotExist:
            return Response( "file ni ", status=status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(files, many=True,context= {'request':request})
        return Response(serializer.data)

class FileDetailView(APIView):
    def get(self,request,p_id,f_id):
        try:
            file = File.objects.get(product_id=p_id,pk=f_id)
        except File.DoesNotExist:
            return Response( "file ni ", status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(file, context= {'request':request})
        return Response(serializer.data)