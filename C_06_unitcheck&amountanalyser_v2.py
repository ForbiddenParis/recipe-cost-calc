def not_blank(question):
    """Checks that a user response is not blank"""


    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def unit_check(choice, options):
    for var_list in options:
        # If the user's unit is anywhere in that row of valid units
        if choice in var_list:
            return var_list[0].lower() # Return the shorthand (e.g., "g")
    return "invalid choice"


def amount_analyser(question):
    """Asks for amount and unit, validates them, and coverts them to base (g, ml)"""
    conversions = {
        "g": 1, "kg": 1000, "ml": 1, "l": 1000, "eggs": 1
    }


    valid_units = [
        ["g", "grams", "gram"],
        ["kg", "kilograms", "kilo"],
        ["ml", "millilitres", "ml"],
        ["l", "litres", "liter"],
        ["eggs", "egg"]
    ]
    while True:
        desired_unit = ""
        desired_amount = ""

        # ask user for ingredient amount and unit
        ingredient_amount = not_blank(question)

        # separate amount and unit
        for item in ingredient_amount:

            if item.isdigit() or item == ".":
                desired_amount = desired_amount + item

            else:
                desired_unit = desired_unit + item

        # takes off extra space and makes units in lowercase
        desired_amount = desired_amount.strip()
        desired_unit = desired_unit.strip().lower()

        # check if unit is valid
        unit = unit_check(desired_unit, valid_units)

        if desired_amount == "":
            amount = "invalid choice"
        else:
            amount = float(desired_amount)

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

        # calculate amounts
        calc_amount = amount * conversions[unit]

        # format amount for good output
        output_amount = f"{amount} {unit}"

        return calc_amount, output_amount

# main
# Test with a normal ingredient

ing = ""
while ing != "xxx":
    ing = not_blank("Ingredient: ")

    if any(i.isdigit() for i in ing):
        print("Error, please enter a valid ingredient")
        continue

    calc_needed, output_needed = amount_analyser(f"Amount of {ing} needed: ")
    print(f"Calculated (in grams/ml): {calc_needed:.2f}")
    print(f"Formatted Output: {output_needed}\n")

    calc_bought, output_bought = amount_analyser(f"Amount of {ing} bought: ")
    print(f"Calculated (in grams/ml): {calc_bought:.2f}")
    print(f"Formatted Output: {output_bought}\n")





