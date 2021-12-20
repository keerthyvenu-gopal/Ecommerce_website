from django.db import models
from shop.models import *
# Create your models here.
class cartlists(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='cartlists'
        ordering=['date']

    def __str__(self):
        return self.cart_id

class item(models.Model):
    prod=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlists,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='item'

    def __str__(self):
        return self.prod

    def total(self):
        return self.prod.price*self.quan

    def total(self):
        return self.prod.price * self.quan