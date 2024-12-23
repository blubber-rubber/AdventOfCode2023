import time
from itertools import combinations

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

expansion = 1000000

empty_rows = []
empty_cols = []

grid = []

for y, line in enumerate(lines):
    line = [x for x in line]
    grid.append(line)
    if all(p == '.' for p in line):
        empty_rows.append(y)

n_cols = len(grid[0])

for col_n in reversed(range(n_cols)):
    if all(grid[y][col_n] == '.' for y in range(len(grid))):
        empty_cols.append(col_n)

galaxies = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            galaxies.append((y, x))

result = 0


for p1, p2 in combinations(galaxies, r=2):
    y1, x1 = p1
    y2, x2 = p2

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    x_empty = len([x for x in empty_cols if x1 < x < x2])
    y_empty = len([y for y in empty_rows if y1 < y < y2])

    result += abs(x2 - x1) + (expansion - 1) * x_empty + abs(y2 - y1) + (expansion - 1) * y_empty

print(result)
print(time.time() - start_time)
