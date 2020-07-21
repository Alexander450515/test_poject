from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True)  # null=True - все созданные ранее User получат пустого юзера
    products = models.ManyToManyField(Product)