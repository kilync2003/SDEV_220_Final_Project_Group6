"""
Edgar Rodriguez
Menu.py

Menu options

Needs lunch / dinner, section for (beverages, sides, and entrees), sales tax

"""


class MenuItem:
    def __init__(self, name, description, price):
        self.name = name # Name displayed on menu
        self.description = description # Description of the dish / beverage
        self.price = price # Price of the menu item


class Menu:
    def __init__(self):
        self.menu_items = {} # Dictionary created for the menu items


    def add_menu_item(self, item_name, description, price):
        if item_name not in self.menu_items: # When the item_name does not match with the menu_items ---
            self.menu_items[item_name] = MenuItem(item_name, description, price) # --- The unmatched item_name will be added to the Menu with the description and price included
        else:
            return("Item already exists in the menu.") # item_name matches with menu_items, nothing happens due to current existence
    

    def remove_menu_item(self, item_name):
        if item_name in self.menu_items: # item_name matches menu_item ---
            del self.menu_items[item_name] # --- Removes matching item_name from menu_item
        else:
            return ("Item not found in the menu.") # Nothing to remove if item_name has no match in menu_item
    

class Order:
    def __init__(self):
        self.items = {} # order items dictionary


    def add_item(self, item_name, quantity):
        if item_name in self.items: # item_name is in items ---
            self.items[item_name] += quantity # items updates by adding to the quantity determined by customer
        else:
            self.items[item_name] = quantity # item_name is not found in items then quantity is empty
    

    def remove_item(self, item_name, quantity):
        if item_name in self.items: # item_name found in items
            self.items[item_name] -= quantity # quantity decreased by the amount specified by customer
            if self.items[item_name] <= 0: # if the quantity is less than or equal to zero ---
                del self.items[item_name] # --- items fully removed from order
        else:
            return ("Item not found in the order.") # item_name not found in items
        
    
    def calculate_total(self, menu):
        total = 0 # Total balance for the order will always start at 0
        for item_name, quantity in self.items.items(): # item_names and quantities found in the dictionary list of items ---
            if item_name in menu.menu_items: # --- When the item_name is in the menu_items
                total += menu.menu_items[item_name].price * quantity # Total is the price of the item_names in the menu_items multiplied by the quantities of each
        return total # The calculated total
    

# Sample of menu items being added to the menu
menu = Menu()
menu.add_menu_item("Teriyaki chicken", "Tender chicken marinated in sweet and savory teriyaki sauce and then grilled to perfection (Side included).", 11.99)
menu.add_menu_item("Mango Smoothie", "Best mango smoothie in the world", 2.99)
menu.add_menu_item("Hot honey glazed salmon", "Alaskan salmon marinated in a hot honey sauce, pan seared (Side included)", 15.99)

# Sample of items being added to the order
order = Order()
order.add_item("Teriyaki chicken", 1)
order.add_item("Hot honey glazed salmon", 2)
order.add_item("Mango Smoothie", 4)

# Getting the final price of the customer's order
total_price = order.calculate_total(menu)
print(f"Total price: ${total_price}") # Customer's final price