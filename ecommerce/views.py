from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView

class HomeView(ListView):
    model = Item
    template_name = "home.html"
