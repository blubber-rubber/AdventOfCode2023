import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

INVENTORY = {'red': 12, 'green': 13, 'blue': 14}

result = 0
for line in lines:
    game, line = line.split(':')
    parts = line.split(';')


    possible = True
    for p in parts:
        for n, color in [combo.strip().split(' ') for combo in p.strip().split(',')]:
            possible = possible and int(n) <= INVENTORY[color]
    if possible:
        result += int(game.split(' ')[-1])

print(result)
print(time.time() - start_time)
