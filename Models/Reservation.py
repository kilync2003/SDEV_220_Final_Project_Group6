class Reservation:
    # Internal class, use the Reservations class instead
    def __init__(self, name, num_customers, reservation_date, reservation_time):
        self.name = name
        self.num_customers = num_customers
        self.reservation_date = reservation_date
        self.reservation_time = reservation_time

    def new_reservation(self, name, num_customers, reservation_date, reservation_time):
        self.name = name
        self.num_customers = num_customers
        self.reservation_date = reservation_date
        self.reservation_time = reservation_time

    def modifying_reservation(self, name, num_customers, reservation_date, reservation_time):
        self.name = name
        self.num_customers = num_customers
        self.reservation_date = reservation_date
        self.reservation_time = reservation_time

    def update_name(self, name):
        self.name = name

    def update_num_customers(self, num_customers):
        self.num_customers = num_customers

    def update_reservation_date(self, new_reservation_date):
        self.reservation_date = new_reservation_date

    def update_reservation_time(self, new_reservation_time):
        self.reservation_time = new_reservation_time
