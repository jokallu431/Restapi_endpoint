from django.db import models

class CsvData(models.Model):
    Manufacturer = models.CharField(max_length=150)
    Price = models.CharField(max_length=50)
    MPG = models.CharField(max_length=50)

