import random


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


def secret_num(var_low_num, var_high_num):
    number = random.randint(var_low_num, var_high_num)
    return number


already_guessed = []

low_num = 0
high_num = 10
guesses_allowed = 5

guessing_num = secret_num(low_num, high_num)


# Set guesses used to zero ath the start of round

guesses_used = 0

guess = ''
# start guessing loop

while guess != guessing_num and guesses_used < guesses_allowed:
    guess = int_checker("What number do you guess? ", low_num, high_num, "xxx")

    if guess == "xxx":
        # set end_game to use so that outer loop can be broken
        end_game = "yes"
        break

    if guess in already_guessed:
        print(f"You've already guessed {guess}. You still have {guesses_used} / {guesses_allowed} guesses")
        continue

    else:
        already_guessed.append(guess)
        guesses_used += 1

        if guess < guessing_num and guesses_used < guesses_allowed:
            feedback = f"That number is too low! You've used {guesses_used} / {guesses_allowed} guesses"

        elif guess > guessing_num and guesses_used < guesses_allowed:
            feedback = f"That number is too high! You've used {guesses_used} / {guesses_allowed} guesses"

        # When the secret number is guessed, we have three different feedback option - lucky, phew, well done

        elif guess == guessing_num:

            if guesses_used == 1:
                feedback = "🍀🍀 Lucky! You got it on the first guess. 🍀🍀"

            elif guesses_used == guesses_allowed:
                feedback = f"Phew! you got it in {guesses_used} guesses"
            else:
                feedback = f"Well done! you guessed the secret number in {guesses_used} guesses"
        # If there are no guesses left!
        else:
            feedback = "You've run out of guesses! You have lost this round."

        print()
        print(feedback)
        print()

        # Additional feedback (warn user they are running out of guesses)

        if guesses_used == guesses_allowed - 1:
            print()
            print("💣 Careful! You only have one guess left! 💣")




