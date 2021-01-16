import base64
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
phone_regex = RegexValidator(regex=r'/^(?:\(?(?:\+?61|0)4\)?(?:[ -]?[0-9]){7}[0-9]$)/',
                             message="Phone number must be entered in the format: '+61999999999'. Up to 11 digits allowed.")


class Customer(models.Model):
    name = models.CharField(max_length=60, null=False)
    phone_number = models.CharField( max_length=17, blank=False, unique=True)  # validators should be a list
    email = models.EmailField(max_length = 254, unique=True)
    is_active = models.BooleanField(default=True)
    is_cart_empty = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=60, null=False)
    logo = models.TextField(blank=False)
    description = models.TextField(blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def set_logo(self, logo):
        self.logo = base64.encodebytes(logo)

    def get_logo(self):
        return base64.decodebytes(self.logo)

class Category(models.Model):
    name = models.CharField(max_length=60, null=False)
    type = models.CharField(max_length=60, null=False, default='Grocery' )
    sub_type = models.CharField(max_length=60, null=False,default='-')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60, null=False)
    image = models.TextField(blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def set_image(self, image):
        self.logo = base64.encodebytes(image)

    def get_image(self):
        return base64.decodebytes(self.image)

class Product_details(models.Model):
    GRAMS = 'grams'
    product = models.ForeignKey('Product',related_name='prod_details', on_delete=models.CASCADE)
    units_in_stock = models.PositiveIntegerField()
    unit = models.CharField(max_length=20, null=False, default=GRAMS)
    unit_weight = models.DecimalField(max_digits=10, decimal_places=2,help_text="Enter the weight in grams")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2 ,help_text="Enter the value in format dollars.cents")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product)

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_paid = models.BooleanField(default=True)
    payment_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    address_id = models.ForeignKey('Address', on_delete=models.CASCADE)

    def __str__(self):
        return self.customer

class Order_details(models.Model):
    product_details_id = models.ForeignKey('Product_details', on_delete=models.CASCADE)
    units_purchased = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_details_id

class Address(models.Model):
    address_line_1 = models.TextField(null=False)
    address_line_2 = models.TextField(null=True)
    city = models.CharField(max_length=50, null=False)
    post_code = models.PositiveIntegerField()
    country = models.CharField(max_length=50,null=False)
    contact = models.CharField( max_length=17, blank=False, unique=True)  # validators should be a list
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)

    def __str__(self):
        return self.address_line_1

class Cart(models.Model):
    product_id = models.ForeignKey('Product_details', on_delete=models.CASCADE)
    units_purchased = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)