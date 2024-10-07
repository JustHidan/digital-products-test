from rest_framework import serializers

from products.models import Product, File, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title','description','avatar')



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields= ('id', 'title','file')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title','description','avatar','categories','files','url')

