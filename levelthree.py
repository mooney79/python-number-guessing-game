from random import randint


def comp_play():
    lucky_number = input('Enter the number for the computer to guess: ')
    guesses = 0
    computer_guess = 11
    top_range = 10
    bottom_range = 1


    while computer_guess != int(lucky_number):
        computer_guess = randint(bottom_range, top_range)
        if computer_guess > int(lucky_number):
            print("Too high!")
            print(computer_guess)
            top_range = computer_guess - 1
            guesses = guesses + 1
        elif computer_guess < int(lucky_number):
            print("Too low")
            print(computer_guess)
            bottom_range = computer_guess + 1
            guesses = guesses + 1
        else:
            print("The computer guessed it on its " + str(guesses+1) + " try!")
            print(computer_guess)

comp_play()