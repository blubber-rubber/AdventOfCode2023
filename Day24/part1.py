import time
from itertools import combinations
import numpy as np

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

hailstones = []

min_test = 200000000000000
max_test = 400000000000000

for line in lines:
    pos, velo = line.strip().split('@')

    pos = tuple(int(x) for x in pos.strip().split(', '))
    velo = tuple(int(x) for x in velo.strip().split(', '))

    hailstones.append((pos, velo))


def get_position(start_position, velocity, time):
    return tuple(start_position[i] + time * velocity[i] for i in range(3))


result = 0
for h1, h2 in combinations(hailstones, r=2):
    p1, v1 = h1
    p2, v2 = h2

    A = np.matrix([[v1[0], -v2[0]], [v1[1], -v2[1]]])
    b = np.matrix([[p2[0] - p1[0]], [p2[1] - p1[1]]])

    if np.linalg.det(A) != 0:
        s = np.linalg.solve(A, b)
        k = s[0, 0]
        l = s[1, 0]

        pos1 = get_position(p1, v1, k)
        pos2 = get_position(p2, v2, l)

        if k >= 0 and l >= 0:
            if min_test <= pos1[0] <= max_test and min_test <= pos1[1] <= max_test:
                result += 1

print(result)
print(time.time() - start_time)
