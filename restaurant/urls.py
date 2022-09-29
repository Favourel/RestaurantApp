from django.urls import path
from . import views as product_view

urlpatterns = [
    path("", product_view.index, name="home"),
    path("<int:pk>/add-to-cart/", product_view.add_to_cart, name="add-to-cart"),
    path("<int:pk>/remove-from-cart/", product_view.remove_from_cart, name="remove-from-cart"),
    path("cart/", product_view.cart, name="cart"),

]