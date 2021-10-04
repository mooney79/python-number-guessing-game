from random import randint

def play():
    lucky_number = randint(1,10)
    guesses_remaining = 3

    while guesses_remaining > 0:
        my_guess = input("Guess a number between 1 and 10: ")
        if int(my_guess) == lucky_number:
            print("Correct!  You win!")
            break
        elif int(my_guess) > lucky_number:
            print("Too high!")
            guesses_remaining = guesses_remaining -1
        else:
            print("Too low")
            guesses_remaining = guesses_remaining -1

if __name__ == '__main__':
    play()