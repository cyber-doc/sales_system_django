from django.db import models

# Create your models here.


class Products(models.Model):
    barcode = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=500)
    count = models.PositiveIntegerField(null=False)
    buy_price = models.PositiveIntegerField(null=False)
    sell_price = models.PositiveIntegerField(null=False)
