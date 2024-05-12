from django import forms
from .models import Reservation, OrderItem, MenuItem


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'number_of_guests', 'reservation_time']
        widgets = {
            'reservation_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']
