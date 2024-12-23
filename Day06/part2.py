import time

import math

start_time = time.time()

# -s**2 +  ts -d >0
# s1 = (t-(t**2-4d)**.5)/2
# s2 = (t+(t**2-4d)**.5)/2

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

t = int(lines[0].split(':')[1].replace(' ',''))
d = int(lines[1].split(':')[1].replace(' ',''))

s1 = math.ceil((t - (t ** 2 - 4 * d) ** .5) / 2)
s2 = math.floor((t + (t ** 2 - 4 * d) ** .5) / 2)


result = s2 - s1 + 1

print(result)

print(time.time() - start_time)
