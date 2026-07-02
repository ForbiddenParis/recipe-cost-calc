
def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print("Please answer yes / no (y / n)")

# main
user_response = ""
# looping
while user_response != "xxx":
    user_response = yes_no_check("Do you want to see the instructions? ")
    print()