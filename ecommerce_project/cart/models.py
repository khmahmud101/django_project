from django.db import models
from products.models import Product

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

class Cart(models.Model):

    items = models.ManyToManyField(CartItem,null=True,blank=True)
    products = models.ManyToManyField(Product,null=True,blank=True)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
