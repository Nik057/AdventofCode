import numpy as np
# list all values, from txt file
values = np.array([l.strip(',') for l in open('day2_data.txt')])

sum_of_points = 0
for i in range(0, len(values)):  # 1-rock, 2-paper, 3-scissors
    # A for Rock, B for Paper, and C for Scissors.
    # X for Rock, Y for Paper, and Z for Scissors
    if values[i] == 'C X':
        sum_of_points = sum_of_points + 1 + 6
    elif values[i] == 'C Y':
        sum_of_points = sum_of_points + 2 + 0
    elif values[i] == 'C Z':
        sum_of_points = sum_of_points + 3 + 3
    elif values[i] == 'B X':
        sum_of_points = sum_of_points + 1 + 0
    elif values[i] == 'B Y':
        sum_of_points = sum_of_points + 2 + 3
    elif values[i] == 'B Z':
        sum_of_points = sum_of_points + 3 + 6
    elif values[i] == 'A X':
        sum_of_points = sum_of_points + 1 + 3
    elif values[i] == 'A Y':
        sum_of_points = sum_of_points + 2 + 6
    elif values[i] == 'A Z':
        sum_of_points = sum_of_points + 3 + 0

print(sum_of_points)
