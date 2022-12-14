# list all values, from txt file, including the '' values
values = [l.strip() for l in open('day1_data.txt')]

elf_dict = {}
# max_value contains the max cal found
list_max = []
counter1 = 0  # to keep track of index in dictionary

for cal_val in ('\n'.join(values)).split('\n\n'):  # for each value separated by double /n
    sum = 0  # sum each value (calories) of one elf
    elf_dict[counter1] = {}  # new value of the dictionary
    elf_dict[counter1]['elf_id'] = counter1  # save elf id

    counter2 = 0  # to keep track of index in dictionary
    for x in cal_val.split('\n'):  # sum and store (not necessary) in dictionary each value of calories per elf
        sum += int(x)
        elf_dict[counter1][counter2] = {}
        elf_dict[counter1][counter2][f'cal_item_{counter2}'] = x
        counter2 += 1

    elf_dict[counter1]['totcal'] = sum  # save sum of calories

    counter1 += 1
for key in range(0, len(elf_dict)):
    # generate a list ordered by greates num of call (decreasing)
    list_max.append(elf_dict[key]['totcal'])
merged = sorted(list_max, reverse=True)

print(f"the max calorie value found is: {merged[0]} "
      f"and the sum of the first 3 cal ammount is: {merged[0] + merged[1] + merged[2]}")

