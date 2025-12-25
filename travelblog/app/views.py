from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from .models import Destination, Hotel, Blog, UserProfile, Booking
from .forms import UserUpdateForm, ProfileUpdateForm, BookingForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

def hotel(request):
    hotels = Hotel.objects.all()
    
    place = request.GET.get('place')
    price_limit = request.GET.get('price_limit')
    
    if place:
        hotels = hotels.filter(
            Q(name__icontains=place) | Q(location__icontains=place)
        )
    
    if price_limit:
        try:
            price_limit = int(price_limit)
            hotels = hotels.filter(price__lte=price_limit)
        except ValueError:
            pass
            
    return render(request, 'hotel.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotel_detail.html', {'hotel': hotel})

def destination(request):
    destinations = Destination.objects.all()
    
    place = request.GET.get('place')
    price_limit = request.GET.get('price_limit')
    
    if place:
        destinations = destinations.filter(
            Q(name__icontains=place) | Q(location__icontains=place)
        )
    
    if price_limit:
        try:
            price_limit = int(price_limit)
            destinations = destinations.filter(price__lte=price_limit)
        except ValueError:
            pass
            
    return render(request, 'destination.html', {'destinations': destinations})

def destination_detail(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    return render(request, 'destination_detail.html', {'destination': destination})

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
            
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required
def profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'profile.html', {'bookings': bookings})

@login_required
def profile_edit(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile_edit.html', context)

@login_required
def book(request, model_type, id):
    if model_type == 'destination':
        content_object = get_object_or_404(Destination, pk=id)
    elif model_type == 'hotel':
        content_object = get_object_or_404(Hotel, pk=id)
    else:
        return redirect('index')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.content_object = content_object
            booking.save()
            messages.success(request, 'Booking successful!')
            return render(request, 'booking_success.html', {'booking': booking})
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form, 'object': content_object})
