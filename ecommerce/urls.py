from django.urls import path, include
from .views import HomeView, ItemDetailView

urlpatterns = [    
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('product/<slug>/', ItemDetailView.as_view(), name='product')
]