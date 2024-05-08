from django.urls import path
from .views import menu, add_item, remove_item, orders, reservations, home

urlpatterns = [
    path('menu/', menu, name='menu'),  # Updated to include 'menu/'
    path('add_item/', add_item, name='add_item'),
    path('remove_item/<int:item_id>/', remove_item, name='remove_item'),
    path('orders/', orders, name='orders'),
    path('reservations/', reservations, name='reservations'),
    path('home/', home, name='home'),
]
