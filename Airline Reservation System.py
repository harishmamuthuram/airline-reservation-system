plane={}
departure=input("Departure: ")
arrival=input("Arrival: ")
date=input("Date of travel: ")

while True:
        print("Please choose an option: ")
        print("1. Reserve a Seat")
        print("2. Cancel a Reservation")
        print("3. Display Reservations")
        print("4. Save Reservations")
        print("5. Exit")
        
        a=int(input("Enter a choice: "))
    
        if a == 1:
            row  = int(input("Enter a row: "))
            column  = int(input("Enter a seat number: "))
            seat = (row - 1) * 6 + column - 1                      
        
            if seat in plane:
                name = plane[seat]
                print("Seat", (seat + 1), "has already been reserved by " + plane[seat])
            else:
                name = input("Enter your name: ")
                plane[seat] = name
                print("Seat", (seat + 1), "has been reserved for", name)
                print ((seat + 1)," ", plane[seat])  
                                 
        elif a == 2:
            row = int(input("Row: "))
            column = int(input("Seat: "))
            seat = (row - 1) * 6 + column - 1
            
            if seat in plane:
                del plane[seat]
                print("The reservation for seat", (seat + 1), "has been cancelled.")
                input("Press enter to continue")
            else:
                print("Seat", (seat + 1), "is not currently reserved by anyone.")
                input("Press enter to continue")
                   
        elif a == 3:
            print("Reservations:")
            print("Departing from",departure,"arriving in", arrival, "on",date)
            for key in plane:
                print((key + 1), "\t", plane[key])
                
        elif a == 4:
            print("Airline reservation saved")

        elif a == 5:
            print("Thank you for choosing to fly with us!")
            break
