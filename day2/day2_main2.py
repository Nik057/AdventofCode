import numpy as np
# open file
with open('day2_data.txt') as fp:
    data = [np.array(line.strip().split(' ')) for line in fp]

sum_point = 0
for i in range(0, len(data)):
    # 1-rock, 2-paper, 3-scissors
    # A for Rock, B for Paper, and C for Scissors
    # X for Rock, Y for Paper, and Z for Scissors
    if (data[i][0]) == 'A':
        if (data[i][1]) == 'X':
            data[i][1] = 'Z'
            sum_point = sum_point + 0 + 3

        elif (data[i][1]) == 'Y':
            data[i][1] = 'X'
            sum_point = sum_point + 3 + 1

        elif (data[i][1]) == 'Z':
            data[i][1] = 'Y'
            sum_point = sum_point + 6 + 2

    elif (data[i][0]) == 'B':
        if (data[i][1]) == 'X':
            data[i][1] = 'X'
            sum_point = sum_point + 0 + 1

        elif (data[i][1]) == 'Y':
            data[i][1] = 'Y'
            sum_point = sum_point + 3 + 2

        elif (data[i][1]) == 'Z':
            data[i][1] = 'Z'
            sum_point = sum_point + 6 + 3

    elif (data[i][0]) == 'C':
        if (data[i][1]) == 'X':
            data[i][1] = 'Y'
            sum_point = sum_point + 0 + 2

        elif (data[i][1]) == 'Y':
            data[i][1] = 'Z'
            sum_point = sum_point + 3 + 3

        elif (data[i][1]) == 'Z':
            data[i][1] = 'X'
            sum_point = sum_point + 6 + 1



print(sum_point)
