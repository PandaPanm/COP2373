#Wes Williams
#8/31/24


def sell_tickets():
    # Constants
    max_tickets = 20
    max_tickets_per_buyer = 4

    # Initialize accumulators
    tickets_sold = 0
    total_buyers = 0

    # Inform the user about the ticket sale process
    print("Welcome to the Regal Oakmont 8 Pre-sale for tickets!")
    print(f"A total of {max_tickets} tickets are available. A lot of people are wanting these so get them while they are hot! (meaning hot of the printer)")

    while tickets_sold < max_tickets:
        try:
            # Prompt user for the number of tickets they want to buy
            desired_tickets = int(
                input(f"Enter the number of tickets you wish to purchase (up to {max_tickets_per_buyer}): "))

            # Check if the number of tickets is within the allowed range
            if desired_tickets < 1 or desired_tickets > max_tickets_per_buyer:
                print(
                    f"You can only purchase between 1 and {max_tickets_per_buyer} tickets at a time. Please try again.")
                continue

            # Check if enough tickets are available
            if desired_tickets > (max_tickets - tickets_sold):
                print(f"Sorry, there are only {max_tickets - tickets_sold} tickets left. Please reduce your request.")
                continue

            # Process the ticket purchase
            tickets_sold += desired_tickets
            total_buyers += 1
            remaining_tickets = max_tickets - tickets_sold

            # Display remaining tickets
            print(f"Thank you for your purchase and enjoy the movie!! {remaining_tickets} tickets remain.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    # After the loop ends, all tickets are sold
    print(f"All tickets have been sold.")
    print(f"Total number of buyers: {total_buyers}")


# Run the ticket selling function
if __name__ == "__main__":
    sell_tickets()
