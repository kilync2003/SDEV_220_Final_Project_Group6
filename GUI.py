import tkinter as tk

class MainMenu(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root  # Storing the root window reference
        # Title label
        title = tk.Label(self, text="Restaurant Management System", anchor="n")
        title.pack()
        # Button for Menu
        menuButton = tk.Button(self, text="Menu", command=self.switchToMenu)
        menuButton.pack(side="left", padx=5, anchor="c")
        # Button for accessing orders menu
        ordersButton = tk.Button(self, text="Orders", command=self.switchToOrders)
        ordersButton.pack(side="left", padx=5, anchor="c")
        # Button for accessing reservations menu
        reservationsButton = tk.Button(self, text="Reservations", command=self.switchToReservations)
        reservationsButton.pack(side="left", padx=5, anchor="c")
        self.menu_container = None

    def switchToMenu(self):
        self.clear_current_menu()
        self.menu_container = MenuWindow(self.root)  
        self.menu_container.pack(fill="both", expand=True)  

    def switchToOrders(self):
        self.clear_current_menu()
        self.menu_container = OrdersWindow(self.root)  
        self.menu_container.pack(fill="both", expand=True)  

    def switchToReservations(self):
        self.clear_current_menu()
        self.menu_container = ReservationsWindow(self.root)  
        self.menu_container.pack(fill="both", expand=True)  

    def clear_current_menu(self):
        if self.menu_container:
            self.menu_container.pack_forget()

class MenuWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.menu_items = ["Pizza", "Burger", "Pasta"]
        
        # Title label
        title = tk.Label(self, text="Menu", anchor="c")
        title.pack()
        
        # Display current menu items
        self.menu_label = tk.Label(self, text="\n".join(self.menu_items))
        self.menu_label.pack()
        
        # Entry for adding new menu item
        self.new_item_entry = tk.Entry(self)
        self.new_item_entry.pack()
        
        # Buttons for adding and removing menu items
        add_button = tk.Button(self, text="Add Item", command=self.add_item)
        add_button.pack(side="left", padx=5, anchor="c")
        
        remove_button = tk.Button(self, text="Remove Item", command=self.remove_item)
        remove_button.pack(side="left", padx=5, anchor="c")

    def add_item(self):
        new_item = self.new_item_entry.get()
        if new_item:
            self.menu_items.append(new_item)
            self.update_menu_display()

    def remove_item(self):
        selected_item = self.new_item_entry.get()
        if selected_item in self.menu_items:
            self.menu_items.remove(selected_item)
            self.update_menu_display()

    def update_menu_display(self):
        self.menu_label.config(text="\n".join(self.menu_items))
        self.new_item_entry.delete(0, tk.END)

class OrdersWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        title = tk.Label(self, text="Orders", anchor="c")
        title.pack()

class ReservationsWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        title = tk.Label(self, text="Reservations", anchor="c")
        title.pack()

if __name__ == '__main__':
    root = tk.Tk()
    view = MainMenu(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()