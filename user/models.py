from django.db import models

# Create your models here.
class MenuItems(models.Model):
    item_name = models.CharField(max_length=30)
    item_desc = models.CharField(max_length=50)
    item_type = models.CharField(max_length=30)
    # item_img = models.ImageField(upload_to="media")
    item_price = models.IntegerField(null=True)
