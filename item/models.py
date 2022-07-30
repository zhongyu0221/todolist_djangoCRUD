from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField(max_length=200)

