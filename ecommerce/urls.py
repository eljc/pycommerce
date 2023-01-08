from django.urls import path, include
from django.conf import settings
from .views import (HomeView, 
    ItemDetailView, 
    add_to_cart, 
    remove_from_cart, 
    OrderSummaryView, 
    remove_single_item_from_cart, 
    CheckoutView, 
    PaymentView,
    AddCouponView)

urlpatterns = [    
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart" ),
    path('remove-from-cart/<slug>', remove_from_cart, name="remove-from-cart" ),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary' ),
    path('remove-single-item-from-cart/<slug>', remove_single_item_from_cart, name="remove-single-item-from-cart" ),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    
]
