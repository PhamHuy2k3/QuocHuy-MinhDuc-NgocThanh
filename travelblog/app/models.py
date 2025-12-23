from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='destinations/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    bath_count = models.IntegerField(default=0)
    bed_count = models.IntegerField(default=0)
    amenity = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hotels/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(max_length=20, default='person')
    duration = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    star_rating = models.IntegerField(default=5)
    bath_count = models.IntegerField(default=0)
    bed_count = models.IntegerField(default=0)
    amenity = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
