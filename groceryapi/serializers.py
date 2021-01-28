from rest_framework import serializers

from .models import *
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','name','phone_number','email')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id','name','logo','description','is_active')

class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_category
        fields = ('id','name','category_logo')

class Product_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_details
        fields = ['id','units_in_stock','unit','unit_weight','unit_price']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = ['id','name','main_category','category_logo']

class ProductSerializer(serializers.ModelSerializer):
    prod_details = Product_detailsSerializer(many=True, read_only=True)
    brand = BrandSerializer()
    sub_category = SubCategorySerializer()
    main_category = MainCategorySerializer()
    class Meta:
        model = Product
        fields = ['id','name','image','brand','sub_category','main_category','prod_details']



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

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product_details_id','units_purchased','customer_id']


class UpdatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Updates
        fields = ('id','update_image','description')

class CustomerCartSerializer(serializers.ModelSerializer):
    cart_details = CartSerializer(many=True)
    class Meta:
        model = Customer
        fields = ['id','cart_details','name']
