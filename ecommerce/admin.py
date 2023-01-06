from django.contrib import admin
from .models import Item, Order, OrderItem, Address, UserProfile, Payment, Coupon

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered']

admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(Coupon)
