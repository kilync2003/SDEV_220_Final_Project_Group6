from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', menu, name='menu'),  # Updated to include 'menu/'
    path('add_item/', add_item, name='add_item'),
    path('remove_item/<int:item_id>/', remove_item, name='remove_item'),
    path('orders/', orders, name='orders'),
    path('reservations/', view_reservations, name='reservations'),
    path('home/', home, name='home'),
    path('reservations/add/', add_reservation, name='add_reservation'),
]
