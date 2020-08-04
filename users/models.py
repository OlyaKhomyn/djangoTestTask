from django.db import models
from orders.models import Order
import datetime


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    registration = models.DateField(default=datetime.date.today)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, blank=True, null=True)
