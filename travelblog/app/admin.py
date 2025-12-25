from django.contrib import admin
from .models import Destination, Hotel, Blog, UserProfile, Booking

admin.site.register(Destination)
admin.site.register(Hotel)
admin.site.register(Blog)
admin.site.register(UserProfile)
admin.site.register(Booking)
