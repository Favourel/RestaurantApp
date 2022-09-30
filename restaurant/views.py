from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Product, Order, Review
from django.contrib import messages
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


@api_view(["GET"])
@login_required
def remove_from_cart(request, pk):
    customer = request.user
    product = get_object_or_404(Product, pk=pk)
    order, created = Order.objects.get_or_create(
        customer=customer, product=product, completed=False,
    )
    order.quantity = (order.quantity - 1)
    order.price = (order.quantity * order.product.price)
    order.save()
    if order.quantity <= 0:
        order.delete()
        message_updated = f"'{product.name}' has been removed from your cart"
        return Response(message_updated)


@login_required
def delete_from_cart(request, pk):
    customer = request.user
    product = get_object_or_404(Product, pk=pk)
    order = Order.objects.filter(customer=customer, product=product)
    if order.exists():
        order.delete()
        messages.success(request, f"'{product.name}' has been deleted from your cart")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart(request):
    customer = request.user
    orders = Order.objects.filter(customer=customer, completed=False).order_by("-date_added")
    cart_total = sum([(item.product.price * item.quantity) for item in orders])
    get_cart_items = sum([item.quantity for item in orders])
    context = {
        "orders": orders,
        "get_cart_total": cart_total,
        "get_cart_items": get_cart_items
    }
    return render(request, "restaurant/cart.html", context)


@login_required
def process_order(request):
    orders = Order.objects.filter(
        customer=request.user, completed=False,
    )
    queryset = []
    for item in orders:
        queryset.append(item.completed == True)
        item.completed = True
        item.save()
    messages.success(request, "Order has been successful😉")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
