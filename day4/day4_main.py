import numpy as np

# list all values, from txt file
values_sx = np.array([l.split(',', 1)[0].strip('\n') for l in open('day4_data.txt')])
values_dx = np.array([s.split(',', 1)[1].strip('\n') for s in open('day4_data.txt')])

counter1 = 0
counter2 = 0
for i in range(0, len(values_sx)):
    values_sx_1 = int(np.array([values_sx[i].split('-', 1)[0].strip('\n')]))
    values_sx_2 = int(np.array([values_sx[i].split('-', 1)[1].strip('\n')]))
    values_dx_1 = int(np.array([values_dx[i].split('-', 1)[0].strip('\n')]))
    values_dx_2 = int(np.array([values_dx[i].split('-', 1)[1].strip('\n')]))

    if values_sx_1 <= values_dx_1 and values_sx_2 >= values_dx_2:
        counter1 += 1
    elif values_sx_1 >= values_dx_1 and values_sx_2 <= values_dx_2:
        counter1 += 1

    if values_dx_1 <= values_sx_1 <= values_dx_2 or values_sx_1 <= values_dx_1 and values_sx_2 >= values_dx_2:
        counter2 += 1
    elif values_dx_1 <= values_sx_2 <= values_dx_2 or values_sx_1 >= values_dx_1 and values_sx_2 <= values_dx_2:
        counter2 += 1

print(counter1, counter2)
