import sqlite3
import datetime

# Connect to the SQLite database
conn = sqlite3.connect('restaurant_reservations.db')
c = conn.cursor()

# Create the reservations table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS reservations
             (reservation_time TEXT PRIMARY KEY, name TEXT, num_guests INTEGER)''')

def make_reservation():
    name = input("Enter your name: ")
    num_guests = int(input("Enter the number of guests: "))
    date_str = input("Enter the date (YYYY-MM-DD): ")
    time_str = input("Enter the time (HH:MM): ")

    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    time = datetime.datetime.strptime(time_str, "%H:%M").time()

    reservation_time = datetime.datetime.combine(date, time)
    reservation_time_str = reservation_time.strftime("%Y-%m-%d %H:%M:%S")

    c.execute("SELECT * FROM reservations WHERE reservation_time = ?", (reservation_time_str,))
    existing_reservation = c.fetchone()

    if existing_reservation:
        print("Sorry, this time slot is already reserved.")
    else:
        c.execute("INSERT INTO reservations VALUES (?, ?, ?)", (reservation_time_str, name, num_guests))
        conn.commit()
        print("Reservation confirmed for", name, "on", date_str, "at", time_str, "for", num_guests, "guests.")

def modify_reservation():
    date_str = input("Enter the date of the reservation (YYYY-MM-DD): ")
    time_str = input("Enter the time of the reservation (HH:MM): ")

    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    time = datetime.datetime.strptime(time_str, "%H:%M").time()

    reservation_time = datetime.datetime.combine(date, time)
    reservation_time_str = reservation_time.strftime("%Y-%m-%d %H:%M:%S")

    c.execute("SELECT * FROM reservations WHERE reservation_time = ?", (reservation_time_str,))
    existing_reservation = c.fetchone()

    if existing_reservation:
        name, num_guests = existing_reservation[1], existing_reservation[2]
        print("Current reservation:", name, "for", num_guests, "guests.")

        new_num_guests = int(input("Enter the new number of guests (or 0 to cancel): "))
        if new_num_guests == 0:
            c.execute("DELETE FROM reservations WHERE reservation_time = ?", (reservation_time_str,))
            conn.commit()
            print("Reservation canceled.")
        else:
            c.execute("UPDATE reservations SET num_guests = ? WHERE reservation_time = ?", (new_num_guests, reservation_time_str))
            conn.commit()
            print("Reservation updated for", name, "with", new_num_guests, "guests.")
    else:
        print("No reservation found for the given date and time.")

while True:
    choice = input("Enter 1 to make a reservation, 2 to modify a reservation, or 0 to exit: ")

    if choice == "1":
        make_reservation()
    elif choice == "2":
        modify_reservation()
    elif choice == "0":
        conn.close()
        break
    else:
        print("Invalid choice. Please try again.")