import time
import math
start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

times = [int(x) for x in lines[0].split(':')[1].split(' ') if x != '']
distances = [int(x) for x in lines[1].split(':')[1].split(' ') if x != '']

result = 1
for t, d in zip(times, distances):
    s1 = math.ceil((t - (t ** 2 - 4 * d) ** .5) / 2)
    s2 = math.floor((t + (t ** 2 - 4 * d) ** .5) / 2)
    result *= (s2 - s1 + 1)

print(result)

print(time.time() - start_time)
