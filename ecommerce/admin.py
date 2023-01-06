from django.contrib import admin
from .models import Item, Order, OrderItem, Address, UserProfile, Payment

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(UserProfile)
admin.site.register(Payment)
