from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import *
from .models import *
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class Product_detailsViewSet(viewsets.ModelViewSet):
    queryset = Product_details.objects.all().order_by('product')
    serializer_class = Product_detailsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer

class HomeScreenProducts(APIView):
    pass