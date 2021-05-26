from django.db import models

# Create your models here.
class Customer(models.Model):

    customerName = models.CharField(max_length=100)
    customerEmail = models.EmailField(max_length=254)
    customerMobileNo = models.CharField(max_length=30)
    customerAddress = models.CharField(max_length=200)

    def __str__(self):
        return self.customerName