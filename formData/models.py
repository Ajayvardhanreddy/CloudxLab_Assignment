from django.db import models


class FormData(models.Model):

    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
