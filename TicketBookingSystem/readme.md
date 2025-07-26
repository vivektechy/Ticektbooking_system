# Ticket Booking System (Console-Based)

This is a simple console-based ticket booking system implemented in Python. It allows users to book, cancel, and view the status of seats in a 50-seat arrangement.

## Features

* **Book Tickets:** Users can book available seats by entering the seat number.
* **Cancel Tickets:** Users can cancel previously booked seats.
* **View Seat Layout:** Users can see the current status of all seats (booked or empty).
* **Simple Console Interface:** Easy-to-use menu-driven interface.

## How to Run

1.  **Save the Python code:** Save the Python code (e.g., as `ticket_booking.py`).
2.  **Open a terminal or command prompt.**
3.  **Navigate to the directory** where you saved the file.
4.  **Run the script:** Execute the command `python ticket_booking.py`.

## Code Explanation

### Initialization

* `seats = ["E"] * 50`: This line initializes a list named `seats` with 50 elements, each set to "E" (representing an empty seat).

### Main Loop

* The `while True:` loop creates the main program loop, which keeps the system running until the user chooses to exit.
* The menu is displayed with options to book, view, cancel, or exit.
* The user's choice is taken as input.

### Booking Tickets

* If the user chooses to book a ticket (choice "1"), the program prompts for the seat number.
* Input validation is performed using `isdigit()` to ensure the input is a valid number.
* The program checks if the seat number is within the valid range (1-50).
* It then checks if the selected seat is empty (`seats[seat_number - 1] == "E"`).
* If the seat is empty, it's marked as booked (`seats[seat_number - 1] = "B"`).

### Viewing Seat Layout

* If the user chooses to view the seat layout (choice "2"), the program iterates through the `seats` list.
* For each seat, it prints the seat number and its status ("B" for booked, "E" for empty).
* The output is formatted into rows of 10 seats for better readability.

### Cancelling Tickets

* If the user chooses to cancel a ticket (choice "3"), the program prompts for the seat number.
* Input validation is performed.
* The program checks if the selected seat is booked (`seats[seat_number - 1] == "B"`).
* If the seat is booked, it's marked as empty (`seats[seat_number - 1] = "E"`).

### Exiting

* If the user chooses to exit (choice "4"), the program prints an "Exiting..." message and breaks out of the loop.

### Input Validation

* The `isdigit()` method is used to validate that the user input for seat numbers is a numeric value.
* Range checks (`1 <= seat_number <= 50`) are used to ensure seat numbers are within the valid range.

## Improvements

* Add ability to save seat data to a file, so data persists between runs.
* Implement a more user-friendly interface.
* Add features like seat selection by row or section.
* Add error handling for edge cases.
* Add a visual seat layout display.