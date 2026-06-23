# Functions go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"


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


# Main routine goes here

print(make_statement("Recipe Cost Calculator", "📖"))

print()
want_instructions = yes_no_check("Do you want to see the instructions? ")
print()

if want_instructions == "yes":
    instructions()

print()
print("program continues...")