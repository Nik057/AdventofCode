import numpy as np


def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2


def get3string(value1, value2, value3):
    string1, string2, string3 = value1[:len(value1)], value2[:len(value2)], value3[:len(value3)]
    return string1, string2, string3


def priority(v):
    if v == 'a':
        p = 1
    elif v == 'b':
        p = 2
    elif v == 'c':
        p = 3
    elif v == 'd':
        p = 4
    elif v == 'e':
        p = 5
    elif v == 'f':
        p = 6
    elif v == 'g':
        p = 7
    elif v == 'h':
        p = 8
    elif v == 'i':
        p = 9
    elif v == 'j':
        p = 10
    elif v == 'k':
        p = 11
    elif v == 'l':
        p = 12
    elif v == 'm':
        p = 13
    elif v == 'n':
        p = 14
    elif v == 'o':
        p = 15
    elif v == 'p':
        p = 16
    elif v == 'q':
        p = 17
    elif v == 'r':
        p = 18
    elif v == 's':
        p = 19
    elif v == 't':
        p = 20
    elif v == 'u':
        p = 21
    elif v == 'v':
        p = 22
    elif v == 'w':
        p = 23
    elif v == 'x':
        p = 24
    elif v == 'y':
        p = 25
    elif v == 'z':
        p = 26
    elif v == 'A':
        p = 27
    elif v == 'B':
        p = 28
    elif v == 'C':
        p = 29
    elif v == 'D':
        p = 30
    elif v == 'E':
        p = 31
    elif v == 'F':
        p = 32
    elif v == 'G':
        p = 33
    elif v == 'H':
        p = 34
    elif v == 'I':
        p = 35
    elif v == 'J':
        p = 36
    elif v == 'K':
        p = 37
    elif v == 'L':
        p = 38
    elif v == 'M':
        p = 39
    elif v == 'N':
        p = 40
    elif v == 'O':
        p = 41
    elif v == 'P':
        p = 42
    elif v == 'Q':
        p = 43
    elif v == 'R':
        p = 44
    elif v == 'S':
        p = 45
    elif v == 'T':
        p = 46
    elif v == 'U':
        p = 47
    elif v == 'V':
        p = 48
    elif v == 'W':
        p = 49
    elif v == 'X':
        p = 50
    elif v == 'Y':
        p = 51
    elif v == 'Z':
        p = 52
    return p


# list all values, from txt file
values = np.array([l.strip('\n') for l in open('day3_data.txt')])

values_sum = 0
for i in range(0, len(values)):
    s1, s2 = splitstring(values[i])
    a = list(set(s1) & set(s2))
    # print("The common letters are:")
    for j in a:
        # print(j)
        values_sum = values_sum + priority(j)

print("The common letters sum is:", values_sum)


values_sum = 0
for i in range(0, len(values), 3):
    s1, s2, s3 = values[i], values[i+1], values[i+2]
    a = list(set(s1) & set(s2) & set(s3))
    # print("The common letters are:")
    for j in a:
        # print(j)
        values_sum = values_sum + priority(j)

print("The common letters sum is:", values_sum)

