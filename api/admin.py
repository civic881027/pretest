from django.contrib import admin
from api.models import Order,OrderItem,Product

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)