from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    atribute = models.CharField(max_length=20)

    def __str__(self):
        return self.name