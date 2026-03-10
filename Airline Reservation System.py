import pickle
import os

# Initialize or load existing reservations
try:
    with open("plane.dat", "rb") as f:
        plane = pickle.load(f)
except FileNotFoundError:
    plane = {}

print("Welcome to ABC Airways, please proceed to make a booking.")
print()

departure = input("Departure: ").strip()
arrival = input("Arrival: ").strip()
date = input("Date of travel: ").strip()

ticket_price = 500

while True:
    print()
    print("1. Reserve Seats")
    print("2. Cancel booking")
    print("3. Show Reservations")
    print("4. Save Reservations")
    print("5. Exit")
    
    try:
        ch = int(input("Please enter your choice: "))
        print()
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue
    
    if ch == 1:
        try:
            num = int(input("Please enter the number of passengers: "))
            if num <= 0:
                print("Please enter a positive number of passengers.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
            
        for i in range(num):
            name = input("Passenger " + str(i+1) + " name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            seat = input("Seat (format: 12A): ").upper().strip()
            if seat in plane:
                print("Seat", seat, "already booked by", plane[seat]['name'])
            else:
                plane[seat] = {'name': name, 'passenger_no': i+1, 'price': ticket_price}
                print("Booked seat", seat, "for", name)
        total = num * ticket_price
        print("Total price for", num, "passengers is", total)
    
    elif ch == 2:
        seat = input("Please select the seat you would like to cancel: ").upper().strip()
        if seat in plane:
            refund = plane[seat]['price']
            name = plane[seat]['name']
            del plane[seat]
            print("Cancelled booking for", name)
            print("Refund amount:", refund)
        else:
            print("Seat not found in reservations.")
    
    elif ch == 3:
        if plane:
            print("Bookings on", date, "from", departure, "to", arrival)
            for s in plane:
                print("Seat", s, "booked for", plane[s]['name'], "price:", plane[s]['price'])
        else:
            print("No reservations found.")
    
    elif ch == 4:
        try:
            with open("plane.dat", "wb") as f:
                pickle.dump(plane, f)
            print("Reservations saved successfully.")
        except Exception as e:
            print("Error saving reservations:", e)
    
    elif ch == 5:
        print("Thank you for choosing to fly with us!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
