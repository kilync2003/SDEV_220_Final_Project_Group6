

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import datetime
from reservation import make_reservation
app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('restaurant_reservations.db', check_same_thread=False)
c = conn.cursor()
 
# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    if request.method == 'POST':
        # Handle reservation form submission
        name = request.form['name']
        num_guests = request.form['num_guests']
        date_str = request.form['date']
        time_str = request.form['time']
        print(name)
        print(num_guests)
        print(date_str)
        print(time_str)
        make_reservation(name, num_guests, date_str,time_str)
        # Process reservation...
        
    # Render reservations page
        reservation_message = f"Reservation confirmed for {name} on {date_str} at {time_str} for {num_guests} guests."

    return render_template('confirmation.html', message=reservation_message) 


    
if __name__ == '__main__':
    app.run(debug=True)
  
