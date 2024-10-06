from rest_framework import serializers

from products.models import Product, File, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title','description','avatar')

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=true)

    class Meta:
        model = Product
        fields = ('title','description','avatar','categories')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields= ('title','file')


