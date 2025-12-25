from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('hotel/', views.hotel, name='hotel'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('destination/', views.destination, name='destination'),
    path('destination/<int:destination_id>/', views.destination_detail, name='destination_detail'),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('book/<str:model_type>/<int:id>/', views.book, name='book'),
    path('booking/edit/<int:booking_id>/', views.booking_edit, name='booking_edit'),
    path('booking/delete/<int:booking_id>/', views.booking_delete, name='booking_delete'),
]
