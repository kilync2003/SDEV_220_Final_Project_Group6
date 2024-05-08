from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MenuItem, Reservation
from .forms import ReservationForm
from django.views.decorators.http import require_POST


def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})


@require_POST
def add_item(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    if name and price:
        MenuItem.objects.create(name=name, price=price)
    return redirect('menu')


@require_POST
def remove_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    item.delete()
    return redirect('menu')


def home(request):
    return render(request, 'home.html')


def orders(request):
    return render(request, 'orders.html')


def view_reservations(request):
    # Fetch all reservations from the database, ordered by reservation time descending
    reservations = Reservation.objects.all().order_by('-reservation_time')
    return render(request, 'reservations.html', {'reservations': reservations})


def add_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a page that shows reservations
            return redirect('reservations')
    else:
        form = ReservationForm()
    return render(request, 'add_reservation.html', {'form': form})
