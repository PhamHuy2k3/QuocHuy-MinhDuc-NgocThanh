from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'phone', 'address']


from .models import Destination, Hotel

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'image', 'price', 'duration', 'location', 'bath_count', 'bed_count', 'amenity', 'description']

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'image', 'price', 'price_unit', 'duration', 'location', 'star_rating', 'bath_count', 'bed_count', 'amenity', 'description']
