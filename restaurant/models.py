from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=70, null=True, blank=True, default=1)
#     date_added = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.name
#
#     @staticmethod
#     def getAllCategory():
#         return Category.objects.all()


class Product(models.Model):
    name = models.CharField(max_length=220, null=True, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, default=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # All Product get
    @staticmethod
    def getAllProduct():
        return Product.objects.all()

    # Filter Product By Category
    # @staticmethod
    # def getProductByFilter(category_id):
    #     if category_id:
    #         return Product.objects.filter(category=category_id)
    #     else:
    #         return Product.getAllProduct()

    @staticmethod
    def getProductById(productList):
        return Product.objects.filter(id__in=productList)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    completed = models.BooleanField(default=False)


class Review(models.Model):
    customer_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)


# class Reservation(models.Model):
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     email = models.EmailField(max_length=255, blank=True, null=True)
#     people = models.CharField(max_length=255, blank=True, null=True)
#     date = models.CharField(max_length=15, blank=True, null=True)
#     time = models.CharField(max_length=15, blank=True, null=True)
#     date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#
#
#     @staticmethod
#     def timeExits(reservationTime):
#         try:
#             time = Reservation.objects.get(time=reservationTime)
#             return time
#         except:
#             return False
