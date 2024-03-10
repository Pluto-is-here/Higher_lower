def int_checker(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...

    if low is None and high is None:
        error = "Please enter an integer"

    # If the number needs to be more than an integer (ie: rounds / high number)

    elif low is not None and high is None:

        error = f"please enter an integer that is more than / equal to {low}"

    else:
        error = f"Please enter an integer that is between {low} and {high} inclusive"

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            # if response is valid, return it

            # check the integer is not too low...
            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response
            # Checks that the number is more than / equal to 13

        except ValueError:
            print(error)


# main routine goes here

# rounds = "test"
# while rounds != "":
#     rounds = int_checker("Rounds <enter for infinite>: ", low=1, exit_code="")
#     print(f"you asked for {rounds}")

# low_num = int_checker("Low Number? ")
# print(f"you chose a low number of {low_num}")

# high_num = int_checker("High number?", low=1)
# print(f"you chose a high number of {high_num}")

guess = ""
while guess != "xxx":
    guess = int_checker("Guess: ", low=0, high=10, exit_code="xxx")
    print(f"You guessed {guess}")
    print()
    