from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import MenuItem, Reservation, Order, OrderItem
from .forms import ReservationForm, OrderItemForm
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
            return redirect('view_reservations')

    else:
        form = ReservationForm()
    return render(request, 'add_reservation.html', {'form': form})


def delete_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    reservation.delete()
    return redirect('view_reservations')


def create_order(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    order, created = Order.objects.get_or_create(reservation=reservation)
    return redirect('add_order_item', order_id=order.id)


def add_order_item(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            # Check if the item is already in the order
            existing_item = OrderItem.objects.filter(
                order=order, menu_item=form.cleaned_data['menu_item']).first()
            if existing_item:
                # If item exists, increment the quantity
                existing_item.quantity += int(form.cleaned_data['quantity'])
                existing_item.save()
            else:
                # Otherwise, create a new order item
                new_item = form.save(commit=False)
                new_item.order = order
                new_item.save()
            order.calculate_total()  # Update the total for the order
            # Redirect to add more items
            return redirect('add_order_item', order_id=order.id)
    else:
        form = OrderItemForm()
    return render(request, 'add_order_item.html', {'form': form, 'order': order})


def order_details(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_details.html', {'order': order})


def view_orders(request):
    # Fetch only orders that are not completed
    active_orders = Order.objects.filter(is_completed=False)
    return render(request, 'orders.html', {'orders': active_orders})


def create_order(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    # Check if an order already exists for this reservation
    order, created = Order.objects.get_or_create(reservation=reservation)
    if created:
        order.save()
    return redirect('add_order_item', order_id=order.id)


def checkout_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_completed = True
    print(order.reservation_id)
    print(order)
    delete_reservation(request, order.reservation_id)
    order.reservation = None
    order.save()
    return redirect('order_completed', order_id=order.id)


def order_completed(request, order_id):
    return render(request, 'order_completed.html', {'order_id': order_id})
