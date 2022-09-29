from django.shortcuts import render, get_object_or_404
from .models import Product, Order, Review
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


def index(request):
    products = Product.objects.all().order_by("-id")
    context = {
        "products": products
    }
    return render(request, "restaurant/Home.html", context)


@api_view(["GET"])
@login_required
def add_to_cart(request, pk):
    customer = request.user
    updated = False
    if customer:
        product = get_object_or_404(Product, pk=pk)
        order, created = Order.objects.get_or_create(
            customer=customer, product=product, completed=False,
        )
        # orderItem, created = OrderItem.objects.get_or_create(customer=customer, order=order, product=product)
        order.quantity = (order.quantity + 1)
        order.price = (order.quantity * order.product.price)
        order.save()
        if order.quantity > 1:
            updated = True
            message = f'"{product}" quantity has been updated!'
        else:
            updated = True
            message = f'"{product}" has been added to your cart!'

        data = {'updated': updated,
                'message': message,
                }
        return Response(data)
    data = {'updated': updated}
    return Response(data)


@login_required
def remove_from_cart(request, pk):
    customer = request.user
    product = get_object_or_404(Product, pk=pk)
    order, created = Order.objects.get_or_create(
        customer=customer, product=product, completed=False,
    )
    # orderItem, created = OrderItem.objects.get_or_create(customer=customer, order=order, product=product)
    if order.objects.filter(customer=customer, order=order, product=order.product).exists():
        order.delete()
        message_updated = f"'{product.name}' has been removed from your cart"
        return Response(message_updated)


@login_required
def cart(request):
    context = {

    }
    return render(request, "restaurant/cart.html", context)
