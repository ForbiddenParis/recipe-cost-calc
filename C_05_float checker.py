def float_checker(question, category):
    """Checks that user is entering a float"""

    while True:
        # ask user for number and checks if it is valid
        try:
            response = float(input(question))

            # Checks number isn't negative
            if response >= 0:
                return response
            else:
                print(f"Invalid! Please enter a valid {category}!")

        except ValueError:
            print("Invalid number, please enter a valid number!")

# main
float_checker("Enter a number: ", "price")


