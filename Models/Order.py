class Order:
    def __init__(self):
        self.items = {}  # order items dictionary

    def add_item(self, item_name, quantity):
        if item_name in self.items:  # item_name is in items ---
            # items updates by adding to the quantity determined by customer
            self.items[item_name] += quantity
        else:
            # item_name is not found in items then quantity is empty
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:  # item_name found in items
            # quantity decreased by the amount specified by customer
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:  # if the quantity is less than or equal to zero ---
                del self.items[item_name]  # --- items fully removed from order
        else:
            # item_name not found in items
            return ("Item not found in the order.")

    def calculate_total(self, menu):
        total = 0  # Total balance for the order will always start at 0
        # item_names and quantities found in the dictionary list of items ---
        for item_name, quantity in self.items.items():
            if item_name in menu.menu_items:  # --- When the item_name is in the menu_items
                # Total is the price of the item_names in the menu_items multiplied by the quantities of each
                total += menu.menu_items[item_name].price * quantity
        return total  # The calculated total
