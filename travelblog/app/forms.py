from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Booking

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'phone', 'address']

class BookingForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    num_people = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1}), min_value=1)

    class Meta:
        model = Booking
        fields = ['num_people', 'start_date', 'end_date']
