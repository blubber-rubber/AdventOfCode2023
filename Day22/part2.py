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
brick_dict = dict()

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

bricks_directly_below = dict()
bricks_directly_above = dict()

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

    current_brick_directly_above = set()
    current_brick_directly_below = set()
    for x, y, z in product(range(x1, x2 + 1, 1), range(y1, y2 + 1), range(z1, z2 + 1)):
        if (x, y, z - 1) in grid_3d and grid_3d[(x, y, z - 1)] != i:
            current_brick_directly_below.add(grid_3d[(x, y, z - 1)])

        elif z - 1 == 0:
            current_brick_directly_below.add('floor')

        if (x, y, z + 1) in grid_3d and grid_3d[(x, y, z + 1)] != i:
            current_brick_directly_above.add(grid_3d[(x, y, z + 1)])

    bricks_directly_below[i] = current_brick_directly_below
    bricks_directly_above[i] = current_brick_directly_above


def get_chain_reaction(droppers, bricks_to_check):
    while bricks_to_check:
        j = bricks_to_check.pop(0)
        if j not in droppers:
            if not bricks_directly_below[j].difference(droppers):
                droppers.add(j)
                for n in bricks_directly_above[j]:
                    bricks_to_check.append(n)

    return len(droppers)


result = 0
for i, brick in enumerate(dropped_bricks):
    droppers = {i}
    bricks_to_check = list(bricks_directly_above[i])
    r = get_chain_reaction(droppers, bricks_to_check)
    result += r - 1

print(result)
print(time.time() - start_time)
