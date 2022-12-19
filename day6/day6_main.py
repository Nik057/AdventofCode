import numpy as np

# list all values, from txt file
values = np.array([l.strip('\n') for l in open('day6_data.txt')])

counter = 0
for i in range(0, len(values[0])-3):
    if values[0][i] != values[0][i+1] and values[0][i] != values[0][i+2] and values[0][i] != values[0][i+3] \
            and values[0][i+1] != values[0][i+2] and values[0][i+1] != values[0][i+3] \
            and values[0][i+2] != values[0][i+3] and counter == 0:
        print(i+4)
        counter = 1

# second solution using List Slicing + set method
# set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements,
# commonly called Set.
counter = 0
for i in range(len(values[0])):
    if len(set(values[0][i:i+14])) == 14 and counter == 0:
        print(i+14)
        counter = 1
