import django
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone


class CustomerUser(User):
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(
        max_length=255, null=True, blank=True, default='')


class Category(models.Model):
    sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)
    name = models.CharField(max_length=255, default='', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, default="")
    is_sub = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='', blank=True, null=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    # upload_to='static/homepage/images/')
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    ship_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, null=True)
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart(self):
        orderitems = self.orderdetail_set.all()
        total = orderitems.price*orderitems.quantity
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderdetail_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderdetail_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    order_add = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
