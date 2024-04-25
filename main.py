class Restaurant:
    def __init__(self):
        self.time_slot = {}
        self.date_slot = {}
        self.book_tables = {}

    
    def add_time_slot(self, time_slot, availability=True):
        self.time_slot[time_slot] = availability

    def add_date_slot(self, date, availability=True):
        self.date_slot[date] = availability 
    
    def book_tables(self, table_number):
        self.book_table.append(table_number) 
    
restaurant = Restaurant()
