import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def extrapolate(lijst):
    if not all(x == 0 for x in lijst):
        new_lijst = []

        for a, b in zip(lijst, lijst[1:]):
            new_lijst.append(b - a)
        new_part = extrapolate(new_lijst)
        return lijst[0]-new_part

    return 0

result = 0
for line in lines:
    line = [int(x) for x in line.split(' ')]
    result+= extrapolate(line)

print(result)
print(time.time() - start_time)
