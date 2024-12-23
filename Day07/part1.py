import time
from collections import Counter

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']



def calculate_rank(cards, value):
    counter = Counter(cards)
    key_vals = list(sorted([(v, k) for k, v in counter.items()], reverse=True))

    typ = []
    vals = []

    for v, k in key_vals:
        typ.append(v)

    for c in cards:
        vals.append(-1 * CARDS.index(c))

    typ = tuple(typ)
    vals = tuple(vals)

    return (typ, vals, cards, value)

sorted_cards =[]
for line in lines:
    hand, value = line.split(' ')

    rank = calculate_rank(hand, value)

    sorted_cards.append(rank)

sorted_cards.sort()

result = 0
for i,x in enumerate(sorted_cards):
    a, b, cards, value = x
    result += (i+1)*int(value)
print(result)
print(time.time() - start_time)
