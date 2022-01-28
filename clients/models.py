from django.db import models


class Client(models.Model):

    document = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=20 )
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email