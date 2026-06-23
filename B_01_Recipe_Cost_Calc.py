import pandas
from tabulate import tabulate

# Functions go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes / no (y / n)")


def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "ℹ️"))

    print('''
    ''')

def float_checker(question, category):
    """Checks that user is entering a float"""

    while True:
        # ask user for number and checks if it is valid
        try:
            response = float(input(question))

            # Checks number isn't negative
            if response > 0:
                return response
            else:
                print(f"Invalid! Please enter a valid {category}!")

        except ValueError:
            print("Invalid number, please enter a valid number!")

def not_blank(question):
    """Checks that a user response is not blank"""


    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")

def unit_check(choice, options):
    """Checks if users unit response is valid"""
    for var_list in options:
        # If the user's unit is anywhere in that row of valid units
        if choice in var_list:
            return var_list[0].lower() # Return the shorthand (e.g., "g")
    return "invalid choice"

def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)

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
        for i in ingredient_amount:

            if i.isdigit() or i == ".":
                desired_amount = desired_amount + i

            else:
                desired_unit = desired_unit + i

        # takes off extra space and makes units in lowercase
        desired_amount = desired_amount.strip()
        desired_unit = desired_unit.strip().lower()

        # check if unit is valid
        unit = unit_check(desired_unit, valid_units)

        # check if amount is valid
        if desired_amount == "":
            amount = "invalid choice"
        else:
            amount = float(desired_amount)

        #  checks if amount is a negative amount
        if amount < 0:
            amount = "invalid choice"


        # Error message if unit and amount invalid
        if unit == "invalid choice" and amount == "invalid choice":
            print(f"Invalid Choice! Please enter a valid unit and amount"
                  f"Pick from {valid_units}")
            continue

            # Error message if just is unit invalid
        elif unit == "invalid choice":
            print(f"Invalid Choice! Please enter a valid unit"
                  f"Pick from {valid_units}")
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


# lists for panda
all_ing_names = []
all_prices = []
all_need_amounts = []
all_total_amounts = []
all_ing_costs = []

# Data Frame Dictionary
ingredient_info_dict = {
    'Ingredient Name': all_ing_names,
    'Price': all_prices,
    'Amount Needed': all_need_amounts,
    'Amount Total': all_total_amounts,
    'Ingredient Cost': all_ing_costs,
}

# main
ing = ""
recipe_cost = 0

# recipe name and serving size
recipe_name = not_blank("Recipe Name: ")
serving_size = float_checker("Serving size: ", "serving_size")

# looping starts here
while ing != "xxx":

    # asks for users ingredients
    ing = not_blank("Ingredient name: ")

    # end loop if exit code is entered
    if ing == "xxx":
        break
    # if there is any digit in the users response then it's not valid
    elif any(i.isdigit() for i in ing):
        print("Error, please enter a valid ingredient")
        continue
    # adds ingredient name to list if valid
    else:
        all_ing_names.append(ing)

    # calculates and changes
    calc_needed, amount_needed = amount_analyser(f"Amount of {ing} needed: ")
    print(f"Calculated (in grams/ml): {calc_needed:.2f}")
    print(f"Formatted Output: {amount_needed}\n")
    all_need_amounts.append(amount_needed)

    calc_bought, amount_bought = amount_analyser(f"Amount of {ing} bought: ")
    print(f"Calculated (in grams/ml): {calc_bought:.2f}")
    print(f"Formatted Output: {amount_bought}\n")
    all_total_amounts.append(amount_bought)

    ing_price = float_checker(f"Amount of {ing} price: ", "price")
    all_prices.append((currency(ing_price)))
    print(all_prices)

    ing_cost = (ing_price / calc_bought) * calc_needed
    all_ing_costs.append((currency(ing_cost)))

    recipe_cost += ing_cost

cost_per_serving = recipe_cost / serving_size
print(cost_per_serving)

# make panda
ingredients_frame = pandas.DataFrame(ingredient_info_dict)
ing_needed_string = tabulate(ingredients_frame[['Ingredient Name', 'Amount Needed']], headers='keys',
                          tablefmt='psql', showindex=False)
ing_bought_string = tabulate(ingredients_frame[['Ingredient Name', 'Amount Total', 'Price', 'Ingredient Cost']], headers='keys',
                          tablefmt='psql', showindex=False)

# headings / strings...
main_heading_string = make_statement(f"Recipe Cost Calculator", "=")
recipe_name_string = f"Recipe Name: {recipe_name}"
serving_string = f"Serving Size: {serving_size}"
recipe_ing_string = make_statement("Recipe Ingredients", "-")
cost_ing_string = make_statement("Amount of Ingredients Bought and Cost", "-")
recipe_cost_string = make_statement(f"Cost for 1 recipe: ${recipe_cost:.2f}", "-")
serving_cost_string = make_statement(f"Cost per serving: ${cost_per_serving:.2f}", "-")

# lists of strings to be outputted / written to file
to_write = [main_heading_string, "\n", serving_string, recipe_name_string,
            "\n", recipe_ing_string, ing_needed_string,
            "\n", cost_ing_string, ing_bought_string,
            recipe_cost_string, serving_cost_string]

# Print area
print()
for item in to_write:
    print(item)

file_name = f"{recipe_name}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")


