from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_details)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(Product_details)