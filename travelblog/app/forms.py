from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Booking, Destination, Hotel

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'phone', 'address']


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'image', 'price', 'duration', 'location', 'bath_count', 'bed_count', 'amenity', 'description']

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'image', 'price', 'price_unit', 'duration', 'location', 'star_rating', 'bath_count', 'bed_count', 'amenity', 'description']

class BookingForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    num_people = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1}), min_value=1)

    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'num_people']


