import pickle  

f = open("plane.dat", "wb")  
pickle.dump({}, f)  
f.close()  

f = open("plane.dat", "rb")  
plane = pickle.load(f)  
f.close()  

print("Welcome to ABC Airways, please proceed to make a booking.")  
print()  

departure = input("Departure: ")  
arrival = input("Arrival: ")  
date = input("Date of travel: ")  

ticket_price = 500   

while True:  
    print()   
    print("1. Reserve Seats")   
    print("2. Cancel booking")   
    print("3. Show Reservations")   
    print("4. Save Reservations")   
    print("5. Exit")   
    ch = int(input("Please enter your choice: "))
    print()
    
    if ch == 1:   
        num = int(input("Please enter the number of passengers: "))   
        for i in range(num):   
            name = input("Passenger " + str(i+1) + " name: ")   
            seat = input("Seat (like 12A): ").upper()   
            if seat in plane:   
                print("Seat", seat, "already booked by", plane[seat]['name'])   
            else:   
                plane[seat] = {'name': name, 'passenger_no': i+1, 'price': ticket_price}   
                print("Booked seat", seat, "for", name)   
        total = num * ticket_price   
        print("Total price for", num, "passengers is", total)   
    
    elif ch == 2:   
        seat = input("Please select the seat you would like to cancel: ").upper()   
        if seat in plane:   
            refund = plane[seat]['price']   
            name = plane[seat]['name']   
            del plane[seat]   
            print("Cancelled booking for", name)   
            print("Refund amount:", refund)   
    
    elif ch == 3:   
        print("Bookings on", date, "from", departure, "to", arrival)   
        for s in plane:   
            print("Seat", s, "booked for", plane[s]['name'], "price:", plane[s]['price'])   
    
    elif ch == 4:   
        f = open("plane.dat", "wb")   
        pickle.dump(plane, f)   
        f.close()   
        print("Reservations saved.")   
    
    elif ch == 5:   
        print("Thank you for choosing to fly with us!")
        
        break   
    
    else:
        
        break 

