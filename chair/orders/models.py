from django.db import models

# Create your models here.
class SalesOrders(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
