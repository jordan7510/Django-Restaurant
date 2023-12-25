from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MenuItems(models.Model):
    item_name = models.CharField(max_length=30)
    item_desc = models.CharField(max_length=50)
    item_type = models.CharField(max_length=30)
    item_price = models.IntegerField(null=True)
    item_image = models.ImageField(upload_to='', null=True, blank=True)


class ReservationDetails(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, default='')
    phoneNumber = models.CharField(max_length=10,null=True)
    noOfGuests = models.IntegerField(null=True)
    reservationDate = models.DateField(null=True)
    reservationTime = models.CharField(max_length=30)

class OrdersDetails(models.Model):
    itemName = models.CharField(max_length=50)
    itemQty = models.IntegerField(null=True)
    orderedBy = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10,null=True)
    orderStatus = models.CharField(max_length=10,default='PENDING')
    orderDate = models.DateTimeField(default=timezone.now)


class UserReviewModel(models.Model):
    message = models.TextField()
    customer_name = models.CharField(max_length=255)
    stars = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
  