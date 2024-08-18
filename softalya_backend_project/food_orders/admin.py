from django.contrib import admin
from .models import Order, OrderItem, Address  # food_orders uygulamasındaki modeller

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
