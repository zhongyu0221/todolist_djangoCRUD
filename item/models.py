from django.db import models
from datetime import datetime
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField(max_length=200)
    Create_Date = models.DateField(default=datetime.now, blank=True)
    Due_Date = models.DateField()

