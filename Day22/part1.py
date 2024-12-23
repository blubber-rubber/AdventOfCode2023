import time
from collections import defaultdict
from itertools import product
import math

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

bricks = []

structure_top = defaultdict(int)
for line in lines:
    parts = [tuple(int(x) for x in part.split(',')) for part in line.split('~')]
    bottom, top = sorted(parts, key=lambda x: x[2])
    bricks.append((bottom, top))

bricks.sort(key=lambda b: b[0][2])

dropped_bricks = []

for brick in bricks:
    p1, p2 = brick
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    highest_peak = 0

    for x, y in product(range(x1, x2 + 1, 1), range(y1, y2 + 1)):
        level = structure_top[(x, y)]
        if level > highest_peak:
            highest_peak = level
    drop_distance = z1 - highest_peak - 1

    if z1 == z2:
        for x, y in product(range(x1, x2 + 1, 1), range(y1, y2 + 1)):
            structure_top[(x, y)] = z1 - drop_distance

    else:
        structure_top[(x1, y1)] = z2 - drop_distance

    dropped_brick = ((x1, y1, z1 - drop_distance), (x2, y2, z2 - drop_distance))
    dropped_bricks.append(dropped_brick)

grid_3d = dict()

for i, brick in enumerate(dropped_bricks):

    p1, p2 = brick
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    if z1 > z2:
        z1, z2 = z2, z1

    for x, y, z in product(range(x1, x2 + 1, 1), range(y1, y2 + 1), range(z1, z2 + 1)):
        grid_3d[(x, y, z)] = i

supported_by = dict()

for i, brick in enumerate(dropped_bricks):

    p1, p2 = brick
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    if z1 > z2:
        z1, z2 = z2, z1

    brick_supported_by = set()
    for x, y, z in product(range(x1, x2 + 1, 1), range(y1, y2 + 1), range(z1, z2 + 1)):
        if (x, y, z - 1) in grid_3d and grid_3d[(x, y, z - 1)] != i:
            brick_supported_by.add(grid_3d[(x, y, z - 1)])

        elif z - 1 == 0:
            brick_supported_by.add('floor')

    supported_by[i] = brick_supported_by


def is_removable_brick(i):
    for j, brick in enumerate(dropped_bricks):
        if i != j:
            if not supported_by[j].difference({i}):
                return False
    return True


result = 0
for i, brick in enumerate(dropped_bricks):
    if is_removable_brick(i):
        result += 1

print(result)
print(time.time() - start_time)
