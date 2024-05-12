from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Reservation(models.Model):
    # Name of the person making the reservation
    name = models.CharField(max_length=100)
    number_of_guests = models.IntegerField()
    reservation_time = models.DateTimeField()

    def __str__(self):
        return f"Reservation for {self.name} - {self.number_of_guests} guests at {self.reservation_time}"


class Order(models.Model):
    reservation = models.ForeignKey(
        Reservation, on_delete=models.SET_NULL, related_name='orders', null=True, blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    # New field to track order status
    is_completed = models.BooleanField(default=False)

    def calculate_total(self):
        self.total = sum(item.total_price for item in self.items.all())
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(
        max_digits=8, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.menu_item.price
        super().save(*args, **kwargs)
