import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

INVENTORY = {'red': 12, 'green': 13, 'blue': 14}

result = 0
for line in lines:
    game, line = line.split(':')
    parts = line.split(';')

    min_possible = {'red': 0, 'green': 0, 'blue': 0}

    for p in parts:
        for n, color in [combo.strip().split(' ') for combo in p.strip().split(',')]:
            min_possible[color] = max(int(n), min_possible[color])
    result += min_possible['red']*min_possible['green']*min_possible['blue']

print(result)
print(time.time() - start_time)
