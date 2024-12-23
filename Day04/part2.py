import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

result = 0

card_count = defaultdict(lambda: 1)

for i, line in enumerate(lines):
    i1 = i + 1
    n_cards = card_count[i1]

    line = line.split(':')[1].strip()
    winning, my_numbers = line.split('|')
    winning_set = set(winning.strip(" ").split(' '))
    my_set = set(my_numbers.strip(" ").split(' '))
    if '' in winning_set:
        winning_set.remove('')
    if "" in my_set:
        my_set.remove('')
    inter = winning_set.intersection(my_set)

    n_matches = len(inter)
    for j in range(i1 + 1, i1 + 1 + n_matches):
        card_count[j] += n_cards
print(sum(card_count.values()))
print(result)
print(time.time() - start_time)
