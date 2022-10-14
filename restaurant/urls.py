from django.urls import path
from . import views as product_view

urlpatterns = [
    path("", product_view.index, name="home"),
    path("<int:pk>/add-to-cart/", product_view.add_to_cart, name="add-to-cart"),
    path("<int:pk>/remove-from-cart/", product_view.remove_from_cart, name="remove-from-cart"),
    path("<int:pk>/delete-from-cart/", product_view.delete_from_cart, name="delete-from-cart"),
    path("cart/", product_view.cart, name="cart"),
    path("process-order/", product_view.process_order, name="process_order"),
    path("reservation/", product_view.place_reservation, name="process_reservation"),

]