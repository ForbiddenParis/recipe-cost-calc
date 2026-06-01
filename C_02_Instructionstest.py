# Functions go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"


def not_blank_and_valid_ans(question, valid_ans_list=None):
    """Checks that a user response is not blank"""

    while valid_ans_list is None:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")
    else:
        while True:
            response = input(question).lower()
            for item in valid_ans_list:

                # check if the response is the entire word
                if response == item:
                    return item

                # check if it's the first letter
                elif response == item[0]:
                    return item

            print(f"Please  choose an option from {valid_ans_list}")
            continue



def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "ℹ️"))

    print('''

    ''')


# Main routine goes here

print(make_statement("Fund Raising Calculator", "💰"))

print()
want_instructions = not_blank_and_valid_ans("Do you want to see the instructions? ",    ["yes", "no"])
print()
if want_instructions == "yes":
    instructions()

recipe_name = not_blank_and_valid_ans("recipe name:")
print(recipe_name)

print()
print("program continues...")