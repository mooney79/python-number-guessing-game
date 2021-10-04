from random import randint

lucky_number = input('Enter the number for the computer to guess: ')
guesses_remaining = 3



while guesses_remaining > 0:
    computer_guess = randint(1, 10)
    if computer_guess == int(lucky_number):
        print("Correct!  The computer wins!")
        break
    elif computer_guess > int(lucky_number):
        print("Too high!")
        guesses_remaining = guesses_remaining -1
    else:
        print("Too low")
        guesses_remaining = guesses_remaining -1