from django.contrib import admin
from .models import *
# Register your models here.
from django.apps import apps



admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Main_category)
admin.site.register(Sub_category)
admin.site.register(Product)
admin.site.register(Product_details)
admin.site.register(Order)
admin.site.register(Order_details)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(Updates)
