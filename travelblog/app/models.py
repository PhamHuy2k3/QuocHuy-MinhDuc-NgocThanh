from django.db import models
from django.contrib.auth.models import User

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

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/')
    created_at = models.DateField()
    description = models.TextField()
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
