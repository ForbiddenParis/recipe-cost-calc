def ing_name_checker(question):
    while True:
        response = input(question).strip()
        # 1. Check if it's empty first
        if response == "":
            print("Sorry, this can't be blank. Please try again.\n")
            continue

        # 2. Check if it contains numbers
        elif any(i.isdigit() for i in response):
            print("Please enter a valid ingredient (no numbers allowed).")
            continue

        # 3. If it passes both, it's valid!
        return response


user_response = ing_name_checker("Please enter a ingredient: ")
