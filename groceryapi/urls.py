from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'product-details', views.Product_detailsViewSet)
router.register(r'cart',views.CartViewSet)
router.register(r'customer-cart',views.CustomerCartViewset, basename='customer-cart')
router.register(r'customer',views.CustomerViewSet, basename='customer')
router.register(r'updates',views.UpdatesViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]