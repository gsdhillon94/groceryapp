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

class MainCategoryViewSet(viewsets.ModelViewSet):
    queryset = Main_category.objects.all().order_by('name')
    serializer_class = MainCategorySerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class UpdatesViewSet(viewsets.ModelViewSet):
    queryset = Updates.objects.all()
    serializer_class = UpdatesSerializer

class CustomerCartViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerCartSerializer

class SubCategoryViewset(viewsets.ModelViewSet):
    queryset = Sub_category.objects.all()
    serializer_class = SubCategorySerializer