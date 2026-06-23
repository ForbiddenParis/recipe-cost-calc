def not_blank(question):
    """Checks that a user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def unit_check(choice, options):
    """Checks if a user input is valid and returns lowercase and unit_type"""
    for i in range(len(options)):
        # If the user's unit is anywhere in that row of valid units
        if choice in options[i]:
            # returns lowercase of the unit
            lowercase = options[i][0].lower()

            # categories unit type on which row it is in
            if i == 0 or i == 1:
                return lowercase, "weight"
            elif i == 2 or i == 3:
                return lowercase, "volume"
            else:
                return lowercase, "pc"

    return "invalid choice", None


def amount_analyser(question, required_type=None):
    """Asks for amount and unit, validates them, and coverts them to base (g, ml)"""
    conversions = {
        "g": 1, "kg": 1000, "ml": 1, "l": 1000, "pc": 1
    }


    valid_units = [
        ["g", "grams", "gram"],
        ["kg", "kilo", "kilograms", "kilogram"],
        ["ml", "millilitres", "milliliters"],
        ["l", "litres", "liters", "liter", "litre"],
        ["pc", "pieces", "piece", ""]
    ]
    while True:
        desired_unit = ""
        desired_amount = ""

        # ask user for ingredient amount and unit
        ingredient_amount = not_blank(question)

        # separate amount and unit
        for item in ingredient_amount:

            # checks the digits and units in the users answer and separates it
            if item.isdigit() or item == "." or item == "-":
                desired_amount += item

            else:
                desired_unit += item

        # takes off extra space and makes units in lowercase
        desired_amount = desired_amount.strip()
        desired_unit = desired_unit.strip().lower()

        # checking the unit and what unit type it is
        unit, unit_type = unit_check(desired_unit, valid_units)

        # checks if amount is none
        if desired_amount == "":
            amount = "invalid choice"
        # checks if amount is over 0

        else:
            amount = float(desired_amount)

        # checks if amount is over 0
        if amount < 0:
            amount = "invalid choice"


        # Error message if unit and amount invalid
        if unit == "invalid choice" and amount == "invalid choice":
            print("Invalid Choice! Please enter a valid unit and amount")
            continue

        # Error message if just is unit invalid
        elif unit == "invalid choice":
            print("Invalid Choice! Please enter a valid unit")
            continue

        # Error message if just amount is invalid
        elif amount == "invalid choice":
            print("Invalid Choice! Please enter a valid amount")
            continue

        print(required_type)
        print(unit_type)
        # checking if the unit type is matches as the first one entered
        if required_type and unit_type != required_type:
            print(f"\nUnit mismatch! You measured the needed amount in {required_type}")
            print(f"Please use matching {required_type} units for the bought amount\n")
            continue

        # calculate amounts
        calc_amount = amount * conversions[unit]

        # format amount for good output
        output_amount = f"{amount} {unit}"

        return calc_amount, output_amount, unit_type

# main
# Test with a normal ingredient

ing = ""
while ing != "xxx":
    ing = not_blank("Ingredient: ")

    # end loop if exit code is entered
    if ing == "xxx":
        break

    # checks if the user has any digits in their ingredient name (not valid)
    if any(i.isdigit() for i in ing):
        print("Error, please enter a valid ingredient")
        continue

    calc_needed, output_needed, current_unit_type = amount_analyser(f"Amount of {ing} needed: ")
    print(f"Calculated (in grams/ml): {calc_needed:.2f}")
    print(f"Formatted Output: {output_needed}\n")

    calc_bought, output_bought, _ = amount_analyser(f"Amount of {ing} bought: ", required_type=current_unit_type)
    print(f"Calculated (in grams/ml): {calc_bought:.2f}")
    print(f"Formatted Output: {output_bought}\n")






