passengerTuple = ("John", "2A", 580)
# Initialize bookingList as a list of tuples for consistent data
bookingList = [passengerTuple]

print(bookingList) # This will now print [('John', '2A', 580)]

input1 = 0 # Initialize input1 to enter the loop

while input1 != 3:
    print("\n********** MENU *************")
    print("Press 1 for Data")
    print("Press 2 to Book")
    print("Press 3 to Exit")

    try:
        input1 = int(input("Enter your Choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue # Skip to the next loop iteration

    if input1 == 1:
        if not bookingList:
            print("No bookings available.")
        else:
            print("\n--- Current Bookings ---")
            for index, data in enumerate(bookingList):
                print(f"Booking {index + 1}: Name: {data[0]}, Seat: {data[1]}, Price: ${data[2]}")
    elif input1 == 2:
        inpPassengerName = input("Passenger Name: ")
        inpSeat = input("Seat #: ")
        try:
            inpPrice = int(input("Ticket Price: "))
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue # Skip to the next loop iteration

        input2 = input("Write 'Confirm' to Book OR 'Cancel' to cancel booking: ")
        if input2.lower() == "confirm":
            # Append the new booking as a tuple
            bookingList.append((inpPassengerName, inpSeat, inpPrice))
            print("Booking Confirmed.")
        else:
            print("Booking cancelled.")
    elif input1 != 3: # Only print "Invalid Choice!" if not exiting
        print("Invalid Choice!")

print("Exiting program. Thank you!")