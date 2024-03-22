import math

import random


# checks user enters a whole number more than 0 or presses <enter>
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


# checks users answers yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print()
            print("Please choose either yes or no.")
            print()


# calculate max number of guesses allowed

def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_up = math.ceil(max_raw)
    max_guesses = max_up + 1
    return max_guesses


# Instructions

def instructions():
    print(''' 

    *** Instructions ***

    To begin, choose a range for the secret number (a minimum and maximum number) 
    or go with the default game ( 1 - 100 )

    Then, choose the number of rounds, or  press <enter> to play on infinite mode.

    Your goal is to try to guess the secret number without running out of guesses.

    Good luck!

    ''')


# Main routine

# initialise game variable

mode = "regular"
rounds_played = 0
game_history = []
game_stats = []

end_game = "no"

print()
print("👆👆 Higher or lower 👇👇")
print()

want_instructions = yes_no("Do you want to view instructions? ")

if want_instructions == "yes":
    instructions()

# Ask users for number of rounds / infinite mode
num_rounds = int_checker("How many rounds would you like? Push <enter> for infinite mode: ", low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 10

# Get game parameters
low_num = int_checker("Choose a low number to guess from: ")
high_num = int_checker("Choose a high number to guess from: ", low=low_num + 1)

guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds and end_game == "no":

    guesses_used = 0
    already_guessed = []

    if mode == "infinite":
        rounds_heading = f"\n ♾♾♾ Round {rounds_played + 1} (Infinite mode) ♾♾♾"
        num_rounds += 1
    else:
        rounds_heading = f"\n 🕰🕰🕰 Round {rounds_played + 1} (Regular mode) 🕰🕰🕰 "

    print(rounds_heading)
    print()

    guessing_num = random.randint(low_num, high_num)
    print(f"Spoiler alert: {guessing_num}")

    guess = ""

    while guess != guessing_num and guesses_used != guesses_allowed:

        guess = int_checker("What number do you guess? ", low_num, high_num, "xxx")

        # set end_game to use so that outer loop can be broken

        if guess == "xxx":
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

        if guesses_used == guesses_allowed - 1:
            print()
            print("💣 Careful! You only have one guess left! 💣")

    if guesses_used == 1:
        game_result = f" 🍀 Round {rounds_played + 1}: You used {guesses_used} / {guesses_allowed} guesses. Lucky! 🍀"
    elif guesses_used == guesses_allowed:
        game_result = f" 😋 Round {rounds_played + 1}: You used {guesses_used} / {guesses_allowed} guesses. Phew! 😋"
    elif guesses_used > guesses_allowed:
        game_result = f"Round {rounds_played + 1} result : You used {guesses_used} / {guesses_allowed} guesses! You lost"
    else:
        f"Round {rounds_played + 1} result : You used {guesses_used} / {guesses_allowed} guesses."

    if guesses_used == guesses_allowed:
        game_stats.append(guesses_used + 1)
    else:
        game_stats.append(guesses_used)
    print(game_stats)

    game_history.append(game_result)

    rounds_played += 1

# if user chooses infinite mode, add +1 rounds to num rounds so num_rounds is never = to rounds_played

if mode == "infinite":
    num_rounds += 1

# Game loop ends here

if num_rounds == rounds_played:
    Sum = sum(game_stats)
    Min = min(game_stats)
    Max = max(game_stats)
    Average = sum(game_stats) / rounds_played

    print("📈 Game Stats 📉")
    print()
    print(f"Total Score = {Sum}")
    print()
    print(f"Best Score = {Min} \t"
          f"Worst Score = {Max} \t"
          f"Average Score = {Average:.0f}")

    want_history = yes_no("Do you want to view your game history?")

    if want_history == "yes":

        for item in game_history:
            print(item)

    print("Thank you for playing!")
