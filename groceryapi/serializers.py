from rest_framework import serializers

from .models import *
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id','name','logo','description','is_active')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','type','sub_type')

class Product_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_details
        fields = ['units_in_stock','unit','unit_weight','unit_price']

class ProductSerializer(serializers.ModelSerializer):
    prod_details = Product_detailsSerializer(many=True, read_only=True)
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id','name','image','brand','category','prod_details']



class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')

class Order_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order_details
        fields = ('__all__')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('__all__')

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('__all__')
