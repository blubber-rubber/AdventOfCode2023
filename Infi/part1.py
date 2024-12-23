import time
import math

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** .5


result = 0
for line in lines:
    numbers = [int(x.strip('() ')) for x in line.split(',')]
    coords = list(zip(numbers[::2], numbers[1::2]))
    max_distance = max([dist(c, (0, 0)) for c in coords])
    result += max_distance
print(result)
print(time.time() - start_time)
