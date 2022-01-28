from django.db import models


from clients.models import Client
from products.models import Product


class Bill(models.Model):

    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=75)
    nit = models.CharField(max_length=12)
    code = models.CharField(max_length=15, unique=True)
    products = models.ManyToManyField(Product, through='BillProducts')

    def __str__(self):
        return self.code


class BillProducts(models.Model):

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
