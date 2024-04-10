class Ticket:
    counter = 1  # Static field to count tickets
    tickets = []  # List to store ticket objects

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.counter + 2000  # Assigning ticket number
        Ticket.counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.tickets.append(self)

    def submit_ticket(self):
        # Method to submit a ticket
        print("\nTicket Submitted Successfully\n")

        self.print_ticket_info()

    def respond_to_ticket(self, response):
        # Method to respond to a ticket
        self.response = response
        if "Password Change" in self.description:
            self.resolve_password_change()
        else:
            self.status = "Closed"

    def resolve_password_change(self):
        # Method to generate password and resolve password change request
        password = self.staff_id[:2] + self.creator_name[:3]
        self.response = f"New password generated: {password}"
        self.status = "Closed"

    def reopen_ticket(self):
        # Method to reopen a closed ticket
        self.status = "Reopened"

    def print_ticket_info(self):
        # Method to print ticket information
        print("Ticket Information:")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Name of Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Contact Email: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Status: {self.status}\n")

    @staticmethod
    def ticket_stats():
        # Method to calculate and print ticket statistics
        num_total = len(Ticket.tickets)
        num_open = sum(ticket.status == "Open" for ticket in Ticket.tickets)
        num_closed = sum(ticket.status == "Closed" for ticket in Ticket.tickets)
        num_reopened = sum(ticket.status == "Reopened" for ticket in Ticket.tickets)

        print("\nTicket Statistics:")
        print(f"Total Tickets: {num_total}")
        print(f"Open Tickets: {num_open}")
        print(f"Closed Tickets: {num_closed}")
        print(f"Reopened Tickets: {num_reopened}\n")

# Function to display menu options
def display_menu():
    print("\n===== Help Desk Ticketing System =====")
    print("1. Create Ticket")
    print("2. See All Tickets")
    print("3. Respond to Ticket")
    print("4. Submit Ticket")
    print("5. Exit")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nCreating Ticket:")
            staff_id = input("Enter Staff ID: ")
            creator_name = input("Enter Creator Name: ")
            contact_email = input("Enter Contact Email: ")
            description = input("Enter Description: ")
            new_ticket = Ticket(staff_id, creator_name, contact_email, description)
            new_ticket.submit_ticket()

        elif choice == "2":
            print("\nDisplaying All Tickets:")
            for ticket in Ticket.tickets:
                ticket.print_ticket_info()
            Ticket.ticket_stats()

        elif choice == "3":
            print("\nResponding to Ticket:")
            ticket_number = int(input("Enter Ticket Number to Respond: "))
            found_ticket = False
            for ticket in Ticket.tickets:
                if ticket.ticket_number == ticket_number:
                    response = input("Enter Response: ")
                    ticket.respond_to_ticket(response)
                    found_ticket = True
                    print("Ticket Updated Successfully\n")
                    break
            if not found_ticket:
                print("Ticket Number not found.")

        elif choice == "4":
            print("\nSubmitting Ticket:")
            Ticket.ticket_stats()

        elif choice == "5":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()