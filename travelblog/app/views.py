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


# --- Admin manage views ---
from .forms import DestinationForm, HotelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def staff_required(view_func):
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, 'Bạn không có quyền truy cập trang này.')
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return _wrapped

@login_required
@staff_required
def manage(request):
    destinations = Destination.objects.all()
    hotels = Hotel.objects.all()
    return render(request, 'manage.html', {'destinations': destinations, 'hotels': hotels})

# Destination CRUD
@login_required
@staff_required
def destination_list_manage(request):
    destinations = Destination.objects.all()
    return render(request, 'destination_list_manage.html', {'destinations': destinations})

@login_required
@staff_required
def destination_add(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination added successfully.')
            return redirect('destination_list_manage')
    else:
        form = DestinationForm()
    return render(request, 'destination_form.html', {'form': form, 'title': 'Add Destination'})

@login_required
@staff_required
def destination_edit(request, pk):
    dest = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=dest)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination updated successfully.')
            return redirect('destination_list_manage')
    else:
        form = DestinationForm(instance=dest)
    return render(request, 'destination_form.html', {'form': form, 'title': 'Edit Destination'})

@login_required
@staff_required
def destination_delete(request, pk):
    dest = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        dest.delete()
        messages.success(request, 'Destination deleted successfully.')
        return redirect('destination_list_manage')
    return render(request, 'confirm_delete.html', {'object': dest, 'type': 'Destination'})

# Hotel CRUD
@login_required
@staff_required
def hotel_list_manage(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list_manage.html', {'hotels': hotels})

@login_required
@staff_required
def hotel_add(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hotel added successfully.')
            return redirect('hotel_list_manage')
    else:
        form = HotelForm()
    return render(request, 'hotel_form.html', {'form': form, 'title': 'Add Hotel'})

@login_required
@staff_required
def hotel_edit(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hotel updated successfully.')
            return redirect('hotel_list_manage')
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hotel_form.html', {'form': form, 'title': 'Edit Hotel'})

@login_required
@staff_required
def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        messages.success(request, 'Hotel deleted successfully.')
        return redirect('hotel_list_manage')
    return render(request, 'confirm_delete.html', {'object': hotel, 'type': 'Hotel'})
