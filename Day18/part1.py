import time
from collections import defaultdict
from shapely import Polygon

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

visited = defaultdict(list)

cx, cy = (0, 0)

directions = {'U': (0, -1), 'D': (0, 1), 'R': (1, 0), 'L': (-1, 0)}

coords = [(cx, cy)]

for line in lines:
    d, n, color = line.split(' ')
    dx, dy = directions[d]
    cx += int(n) * dx
    cy += int(n) * dy
    coords.append((cx, cy))

poly = Polygon(coords)

print(int(poly.buffer(0.5, join_style='mitre').area))

print(time.time() - start_time)
