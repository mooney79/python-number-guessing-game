selection = ''
count = 0
cpu_count = 0

while True:
    selection = input("Would you like to play(1), or have the computer guess?(2) ^C to quit ")
    selection = int(selection)
    if selection == 1:
        count = count+1
        if count == 1:
            from levelone import play
        else:
            play()
    elif selection == 2:
        cpu_count = cpu_count+1
        if cpu_count == 1:
            from levelthree import comp_play
        else:    
            comp_play()
    else:
        print("Input not recognized.  Please try again")

