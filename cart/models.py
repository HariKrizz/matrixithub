from django.db import models
from shop.models import *


# Create your models here.

class cartList(models.Model):
    cart_id = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class cartItems(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartList, on_delete=models.CASCADE) 
    qty = models.IntegerField()
    active = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.prod
    
    def total(self):
        return (self.prod.price*self.qty)


