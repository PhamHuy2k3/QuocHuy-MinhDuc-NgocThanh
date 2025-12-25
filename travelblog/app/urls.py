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

    # Admin/manage routes
    path('manage/', views.manage, name='manage'),
    path('manage/destinations/', views.destination_list_manage, name='destination_list_manage'),
    path('manage/destinations/add/', views.destination_add, name='destination_add'),
    path('manage/destinations/<int:pk>/edit/', views.destination_edit, name='destination_edit'),
    path('manage/destinations/<int:pk>/delete/', views.destination_delete, name='destination_delete'),

    path('manage/hotels/', views.hotel_list_manage, name='hotel_list_manage'),
    path('manage/hotels/add/', views.hotel_add, name='hotel_add'),
    path('manage/hotels/<int:pk>/edit/', views.hotel_edit, name='hotel_edit'),
    path('manage/hotels/<int:pk>/delete/', views.hotel_delete, name='hotel_delete'),

    # Booking routes
    path('book/<str:content_type>/<int:object_id>/', views.book, name='book'),
    path('book/success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('booking/<int:pk>/edit/', views.booking_edit, name='booking_edit'),
    path('booking/<int:pk>/delete/', views.booking_delete, name='booking_delete'),
]
