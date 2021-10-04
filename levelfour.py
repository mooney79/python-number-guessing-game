from levelone import play
from levelthree import comp_play

selection = ''
count = 0
cpu_count = 0

while True:
    selection = input("Would you like to play(1), or have the computer guess?(2) ^C to quit ")
    selection = int(selection)
    if selection == 1:
        play()
    elif selection == 2:   
        comp_play()
    else:
        print("Input not recognized.  Please try again")

