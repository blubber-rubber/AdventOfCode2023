import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

result = 0

for line in lines:
    line = line.split(':')[1].strip()
    winning, my_numbers = line.split('|')
    winning_set = set(winning.strip(" ").split(' '))
    my_set = set(my_numbers.strip(" ").split(' '))
    if '' in winning_set:
        winning_set.remove('')
    if "" in my_set:
        my_set.remove('')
    inter = winning_set.intersection(my_set)
    if inter:
        score = 2 ** (len(inter) - 1)
        result += score
print(result)
print(time.time() - start_time)
