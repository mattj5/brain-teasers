# Monty Hall problem simulated

import random

all_options = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
win_count = 0
total_simulations = 100
switched_door = -1

for _ in range(total_simulations):
    # pseudo-randomly decide situation
    situation = all_options[random.randint(0,2)]
    
    # choose A
    x = 0
    
    # remove a goat door
    
    if (situation[0] == 1):
        # door A has the car
        switched_door = random.randint(1,2) # door B/C is removed
        x = switched_door # choosing either C/B will result in a loss
    elif (situation[1] == 1):
        # door B has the car
        switched_door = 1 # door C is removed
        x = 1 # choose to switch
    else:
        # door C has the car
        switched_door = 2 # door B is removed
        x = 2 # choose to switch
    
    # switch
    if (situation[x] == 1):
        win_count = win_count + 1


print(win_count)
print("P(win|switch)=",float(win_count/total_simulations))
