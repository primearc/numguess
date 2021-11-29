import random

RIGHT = 6


def welcome():
    correctnum = random.randint(0, 100)
    repeat = RIGHT
    print(f"Welcome to the NUMGUESS.\n \
    You have {repeat} left.\n \
    Have Fun!")
    return correctnum, repeat


def ask():
    guess = input("Please enter your guess: ")
    try:
        return int(guess)
    except ValueError:
        print("Your input is invalid. Please enter the NUMBER!")
        return ask()


def analyze(guess, correctnum, repeat):
    if guess == correctnum:
        print(f"Your guess is true, congratulations! \n Your point: {repeat}")
        end()
    elif guess < correctnum:
        print("UP")
        repeat -= 1
        if repeat == 0:
            print(f"You have no right...\nNumber was {correctnum}")
            end()
        show_status(repeat)
        guess = ask()
        analyze(guess, correctnum, repeat)
    elif guess > correctnum:
        print("DOWN")
        repeat -= 1
        if repeat == 0:
            print(f"You have no right...\nNumber was {correctnum}")
            end()
        show_status(repeat)
        guess = ask()
        analyze(guess, correctnum, repeat)


def show_status(right):
    print(f"You have {right} right.")


def end():
    answer = input("Would you like to play once again? (y/n)").lower()
    if answer == "y":
        return game()
    elif answer == "n":
        return exit("See you later!")
    else:
        print("You typed wrong try again..")
        return end()


def game():
    correct, repeat = welcome()
    guess = ask()
    analyze(guess, correct, repeat)


game()
