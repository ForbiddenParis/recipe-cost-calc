import pandas
from tabulate import tabulate


# Functions go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"

def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "ℹ️"))

    print('''Welcome to Recipe Cost Calculator!

This program helps calculate the total cost of making a recipe and figures out 
cost per serving. It also calculates how much of each ingredient costs for the recipe.

To use it:
- Enter the name of your recipe and serving size.
- For each ingredient, you will be asked to enter:
  - The ingredient name (eg. Milk, Flour, Eggs)
  - The amount needed for the recipe (eg. 250g, 200ml, 5 pc)
  - The total amount bought at the store (eg, 2kg, 1.5L, 10 pc)
  - The price you paid for the amount bought
- When you are finished entering ingredients, type 'xxx' in the ingredient name question to stop.

This program also automatically converts units (such as kg to g and l to ml, or the other way round).
This is to calculate the exact cost of the portion of the ingredient you used.

It will also output:
- A printed breakdown of the ingredients, amounts, and costs.
- The overall cost of the recipe, and cost per serving.
- A saved text file named after the recipe name containing all the data.

Enjoy! 
    ''')

def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:
        # user response
        response = input(question).lower()
        # checking if response is y/n
        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes / no (y / n)")

def not_blank(question):
    """Checks that a user response is not blank"""


    while True:
        # asks user question
        response = input(question)
        # checks if response is blank
        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")

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
                print(f"Please enter a valid {category}! (more than 0)")

        except ValueError:
            print("Please enter a valid number (more than 0)!")

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
        ["pc", "pieces", "piece"]
    ]
    while True:
        desired_unit = ""
        desired_amount = ""

        # ask user for ingredient amount and unit
        ingredient_amount = not_blank(question)

        # separate amount and unit
        for i in ingredient_amount:

            # checks the digits and units in the users answer and separates it
            if i.isdigit() or i == "." or i == "-":
                desired_amount += i

            else:
                desired_unit += i

        # takes off extra space and makes units in lowercase
        desired_amount = desired_amount.strip()
        desired_unit = desired_unit.strip().lower()

        # checking the unit and what unit type it is
        unit, unit_type = unit_check(desired_unit, valid_units)

        # checks if amount is none
        if desired_amount == "":
            amount = "invalid choice"
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

def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)

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

print(make_statement("Recipe Cost Calculator", "📖"))
print()

want_instructions = yes_no_check("Do you want to see the instructions?")
print()

if want_instructions == "yes":
    instructions()

# recipe name and serving size
recipe_name = not_blank("Recipe Name: ")
serving_size = float_checker("Serving size: ", "serving_size")
print()

while ing != "xxx":
    ing = not_blank("Ingredient: ")
    print()

    # end loop if exit code is entered
    if ing == "xxx":
        break
    # checks if the user has any digits in their ingredient name (not valid)
    if any(i.isdigit() for i in ing):
        print("Error, please enter a valid ingredient")
        continue
    # adds ingredient name to list if valid
    else:
        all_ing_names.append(ing)

    # calculates and checks amount needed
    calc_needed, amount_needed, current_unit_type = amount_analyser(f"Amount of {ing} needed: ")
    all_need_amounts.append(amount_needed)

    # calculates and checks amount bought
    calc_bought, amount_bought, _ = amount_analyser(f"Amount of {ing} bought: ", required_type=current_unit_type)
    all_total_amounts.append(amount_bought)

    # asking users for ingredient price
    ing_price = float_checker(f"Amount of {ing} price: ", "price")
    print()
    all_prices.append((currency(ing_price)))

    # ingredient cost for amount needed from amount bought
    ing_cost = (ing_price / calc_bought) * calc_needed
    all_ing_costs.append((currency(ing_cost)))

    # overall recipe costs adding
    recipe_cost += ing_cost

# cost per serving calculation
cost_per_serving = recipe_cost / serving_size

# make panda
ingredients_frame = pandas.DataFrame(ingredient_info_dict)
ing_needed_string = tabulate(ingredients_frame[['Ingredient Name', 'Amount Needed']], headers='keys',
                          tablefmt='fancy_grid', showindex=False)
ing_bought_string = tabulate(ingredients_frame[['Ingredient Name', 'Amount Total', 'Price', 'Ingredient Cost']], headers='keys',
                          tablefmt='fancy_grid', showindex=False)

# headings / strings...
main_heading_string = make_statement(f"Recipe Cost Calculator", "=")
recipe_name_string = f"Recipe Name: {recipe_name}"
serving_string = f"Serving Size: {serving_size}"
recipe_ing_string = make_statement("Recipe Ingredients", "-")
cost_ing_string = make_statement("Amount of Ingredients Bought and Cost", "-")
recipe_cost_string = make_statement(f"Cost for 1 recipe: ${recipe_cost:.2f}", "-")
serving_cost_string = make_statement(f"Cost per serving: ${cost_per_serving:.2f}", "-")

# lists of strings to be outputted / written to file
to_write = [main_heading_string, recipe_name_string, serving_string,
            "\n", recipe_ing_string, ing_needed_string,
            "\n", cost_ing_string, ing_bought_string,"\n",
            recipe_cost_string, serving_cost_string]

# Print area
print()
for item in to_write:
    print(item)

# file name as recipe name
file_name = f"{recipe_name}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+", encoding="utf-8")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
