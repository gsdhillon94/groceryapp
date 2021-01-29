from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import *
from .models import *
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class MainCategoryViewSet(viewsets.ModelViewSet):
    queryset = Main_category.objects.all().order_by('id')
    serializer_class = MainCategorySerializer

class SubCategoryProductViewset(viewsets.ModelViewSet):
    queryset = Sub_category.objects.all().order_by('id')
    serializer_class = SubCategoryProductSerializer

class CustomerCartViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerCartSerializer

class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer