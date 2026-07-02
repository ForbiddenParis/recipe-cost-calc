def unit_checker(question):
    """Checks that the users input valid answers"""
    valid_units = [
        "g", "grams", "gram",
        "kg", "kilograms", "kilo",
        "ml", "millilitres", "ml",
        "l", "litres", "liters",
        "eggs", "egg"
    ]
    while True:

        response = input(question).lower()

        for item in valid_units:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item


        print(f"Please  choose an option from {valid_units}")

def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def not_blank(question):
    """Checks that a user response is not blank"""


    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")

ing = ""
conversions = {
    "g": 1, "kg": 1000, "ml": 1, "l": 1000, "eggs": 1
}

# loop

while ing != "xxx":

    # asking for ingredient
    ing = not_blank("Ingredient: ")

    # breaks loop if xxx
    if ing == "xxx":
        break

    # the amount of the ingredient
    recipe_amount = num_check("Recipe Amount: ")
    # the unit
    recipe_unit = unit_checker("Unit: ")
    print()

    # getting the amount bought
    bought_amount = num_check("Amount Bought: ")
    # getting the anit bought
    bought_unit = unit_checker("Unit: ")
    price_bought = num_check("Price Bought: $")
    print()

    # calculations for units
    amount_needed = recipe_amount * conversions[recipe_unit]
    amount_bought = bought_amount * conversions[bought_unit]
    print(amount_needed)
    print(amount_bought)

    # cost
    cost = (price_bought/amount_bought) * amount_needed
    print(f"${cost}")

