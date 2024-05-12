from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),  # Updated to include 'menu/'
    path('add_item/', add_item, name='add_item'),
    path('remove_item/<int:item_id>/', remove_item, name='remove_item'),
    path('orders/', view_orders, name='view_orders'),
    path('reservations/', view_reservations, name='view_reservations'),
    path('home/', home, name='home'),
    path('reservations/add/', add_reservation, name='add_reservation'),
    path('reservations/delete/<int:reservation_id>/',
         delete_reservation, name='delete_reservation'),
    path('orders/create/<int:reservation_id>/',
         create_order, name='create_order'),
    path('orders/add_item/<int:order_id>/',
         add_order_item, name='add_order_item'),
    path('orders/<int:order_id>/', order_details, name='order_details'),
    path('orders/create/<int:reservation_id>/',
         create_order, name='create_order'),
    path('orders/order_completed/<int:order_id>/',
         order_completed, name='order_completed'),
    path('orders/checkout/<int:order_id>/',
         checkout_order, name='checkout_order'),
]
