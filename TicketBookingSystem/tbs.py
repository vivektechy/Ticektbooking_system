seats = ["E"] * 50

while True:
    print("\nTicket Booking System")
    print("1. Book Ticket")
    print("2. Show Seats")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        seat_number_str = input("Enter seat number (1-50): ")
        if seat_number_str.isdigit():
            seat_number = int(seat_number_str)
            if 1 <= seat_number <= 50:
                if seats[seat_number - 1] == "E":
                    seats[seat_number - 1] = "B"
                    print(f"Seat {seat_number} booked successfully!")
                else:
                    print("Seat already booked.")
            else:
                print("Invalid seat number. Please enter a number between 1 and 50.")
        else:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        print("Seat Layout:")
        for i, seat in enumerate(seats):
            if seats[i] == "B":
                print(f"Seat {i + 1}: B", end=" ")
            else:
                print(f"Seat {i + 1}: E", end="  ")
            if (i + 1) % 10 == 0:
                print()

    elif choice == "3":
        seat_number_str = input("Enter seat number to cancel (1-50): ")
        if seat_number_str.isdigit():
            seat_number = int(seat_number_str)
            if 1 <= seat_number <= 50:
                if seats[seat_number - 1] == "B":
                    seats[seat_number - 1] = "E"
                    print(f"Seat {seat_number} cancelled successfully!")
                else:
                    print("Seat is not booked.")
            else:
                print("Invalid seat number. Please enter a number between 1 and 50.")
        else:
            print("Invalid input. Please enter a number.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")