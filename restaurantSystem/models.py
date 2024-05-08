from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Reservation(models.Model):
    number_of_guests = models.IntegerField()
    reservation_time = models.DateTimeField()

    def __str__(self):
        return f"Reservation for {self.number_of_guests} on {self.reservation_time}"


class Order(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem, through='OrderItem')

    def get_total(self):
        return sum(item.price * item.quantity for item in self.orderitem_set.all())

    def __str__(self):
        return f"Order for Reservation {self.reservation.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"
