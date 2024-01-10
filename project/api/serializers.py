from rest_framework import serializers
from .models import Products, Categories

class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CategoriesSer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'




