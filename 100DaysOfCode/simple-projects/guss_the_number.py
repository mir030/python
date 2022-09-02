import random


def guess_the_number():
    secret_number = random.randint(1, 100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        tries = 10
    elif difficulty == "hard":
        tries = 5

    print(f" You have {tries} tries to guess the correct number")

    counter = 1
    correct_guess = False
    while not correct_guess and counter <= tries:
        guessed_number = int(input("Guess a number between 1 to 100: "))
        if guessed_number > secret_number:
            counter += 1
            print("Too high. Guess again?")
        elif guessed_number < secret_number:
            counter += 1
            print("Too low. Guess again?")
        elif guessed_number == secret_number:
            counter += 1
            print("You got it. Congratulations!!")
            correct_guess = True
    if counter > tries:
        print("You used all of your tries. You lose :(")


guess_the_number()