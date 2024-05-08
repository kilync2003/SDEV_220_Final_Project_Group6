"""
Edgar Rodriguez
Menu.py

Menu options

Needs lunch / dinner, section for (beverages, sides, and entrees), sales tax

"""
import MenuItem


class Menu:
    def __init__(self):
        self.menu_items = {}  # Dictionary created for the menu items

    def add_menu_item(self, item_name, description, price):
        if item_name not in self.menu_items:  # When the item_name does not match with the menu_items ---
            # --- The unmatched item_name will be added to the Menu with the description and price included
            self.menu_items[item_name] = MenuItem(
                item_name, description, price)
        else:
            # item_name matches with menu_items, nothing happens due to current existence
            return ("Item already exists in the menu.")

    def remove_menu_item(self, item_name):
        if item_name in self.menu_items:  # item_name matches menu_item ---
            # --- Removes matching item_name from menu_item
            del self.menu_items[item_name]
        else:
            # Nothing to remove if item_name has no match in menu_item
            return ("Item not found in the menu.")
