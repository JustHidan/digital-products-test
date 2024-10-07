from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductSerializer


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