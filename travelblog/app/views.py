from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Destination, Hotel, Blog, UserProfile
from .forms import UserUpdateForm, ProfileUpdateForm

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
            
    return render(request, 'hotel.html', {'hotels': hotels})-1

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
    return render(request, 'profile.html')

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
