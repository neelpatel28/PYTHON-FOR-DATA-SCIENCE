class RailwayReservationSystem:
    def __init__(self):
        self.available_seats = 10
        self.confirmed = {}
        self.waiting_list = []

    def book_ticket(self, name, age):
        if self.available_seats > 0:
            ticket_id = len(self.confirmed) + 1
            self.confirmed[ticket_id] = {"name": name, "age": age}
            self.available_seats -= 1
            print(f"Ticket confirmed! Ticket ID: {ticket_id}")
        else:
            self.waiting_list.append({"name": name, "age": age})
            print("No seats available. Added to waiting list.")

    def cancel_ticket(self, ticket_id):
        if ticket_id in self.confirmed:
            del self.confirmed[ticket_id]
            self.available_seats += 1
            print("Ticket cancelled successfully.")

            if self.waiting_list:
                person = self.waiting_list.pop(0)
                self.book_ticket(person["name"], person["age"])
        else:
            print("Invalid Ticket ID.")

    def display_status(self):
        print("\nConfirmed Tickets:")
        for tid, info in self.confirmed.items():
            print(tid, info)

        print("\nWaiting List:")
        for w in self.waiting_list:
            print(w)

        print("\nAvailable Seats:", self.available_seats)


system = RailwayReservationSystem()

while True:
    print("\nRailway Reservation System")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Display Status")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        system.book_ticket(name, age)

    elif choice == '2':
        tid = int(input("Enter Ticket ID: "))
        system.cancel_ticket(tid)

    elif choice == '3':
        system.display_status()

    elif choice == '4':
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")
