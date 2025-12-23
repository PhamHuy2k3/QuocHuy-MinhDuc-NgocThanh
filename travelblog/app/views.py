from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from .models import Destination

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def hotel(request):
    return render(request, 'hotel.html')

def destination(request):
    destinations = Destination.objects.all()
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
