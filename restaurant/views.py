from django.shortcuts import render
from .models import Product, Order, Review

# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "restaurant/Home.html", context)
