from django.db import models
from products.models import Product


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
