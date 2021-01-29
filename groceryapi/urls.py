from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'main-categories', views.MainCategoryViewSet, basename="all_main_categories")
router.register(r'category-products', views.SubCategoryProductViewset, basename="all_products")
router.register(r'customer-cart', views.CustomerCartViewset, basename="customer-cart")
router.register(r'cart', views.CartViewset, basename="cart")

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]