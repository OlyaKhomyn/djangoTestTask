from django.contrib import admin

from users.models import User
from orders.models import Order
from products.models import Product

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Product)
