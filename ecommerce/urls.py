from django.urls import path, include
from .views import HomeView, ItemDetailView, add_to_cart, remove_from_cart, OrderSummaryView, remove_single_item_from_cart
from django.conf import settings

urlpatterns = [    
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart" ),
    path('remove-from-cart/<slug>', remove_from_cart, name="remove-from-cart" ),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary' ),
    path('remove-single-item-from-cart/<slug>', remove_single_item_from_cart, name="remove-single-item-from-cart" )
    
]
