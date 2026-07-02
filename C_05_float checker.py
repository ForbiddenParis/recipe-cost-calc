def float_checker(question, category):
    """Checks that user is entering a float"""

    while True:
        # ask user for number and checks if it is valid
        try:
            response = float(input(question))

            # checks number isn't negative
            if response > 0:
                return response
            else:
                print(f"Please enter a valid {category} (more than 0)")

        except ValueError:
            print("Please enter a valid number (more than 0)!")

# main
while True:
    float_checker("Enter a number: ", "price")


