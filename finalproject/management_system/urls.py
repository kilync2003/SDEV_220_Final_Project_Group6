from django.contrib import admin
from django.urls import path
from . import views
#setting urls for pages
urlpatterns = [
    path('',views.home,name='management-home'),
    path('menu/',views.menu,name='management-menu'),
    path('orders/',views.orders,name='management-orders'),
    path('reservations/',views.reservations,name='management-reservations')
]
