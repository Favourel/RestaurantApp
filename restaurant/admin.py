from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["product", "customer", "price", "completed"]
    search_fields = ["customer"]


class ReservationAdmin(admin.ModelAdmin):
    list_display = ["full_name", "people", "check_in_date", "check_in_time"]
    search_fields = ["full_name", "email"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review)
admin.site.register(Reservation, ReservationAdmin)
