from django.db import models
from django.utils import timezone
from django.conf import settings
from django.shortcuts import reverse
from django.core.exceptions import ValidationError

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=220, null=True, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', kwargs={'pk': self.pk})

    def get_delete_to_cart_url(self):
        return reverse('delete-from-cart', kwargs={'pk': self.pk})


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product}"

    def get_total(self):
        total = self.product.price * self.quantity
        return total


class Review(models.Model):
    customer_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name}"


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class Reservation(models.Model):
    RESERVATION_TYPES = (
        ("1 Person", "1 Person"), ("2 People", "2 People"),  ("3 People", "3 People"), ("4 People", "4 People")
    )

    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(max_length=20, blank=True, null=True)
    people = models.CharField(choices=RESERVATION_TYPES, max_length=10)
    check_in_date = models.DateField(null=True, blank=True, default=None, validators=[validate_date])
    check_in_time = models.TimeField(null=True, blank=True, default=None)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.full_name
