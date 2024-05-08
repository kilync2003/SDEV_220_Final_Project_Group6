from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MenuItem
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


def reservations(request):
    return render(request, 'reservations.html')
