import time
from itertools import product

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

grid = []

for line in lines:
    line = [x for x in line]
    grid.append(line)
    if all(p == '.' for p in line):
        grid.append(['.'] * len(line))

n_cols = len(grid[0])

for col_n in reversed(range(n_cols)):
    if all(grid[y][col_n] == '.' for y in range(len(grid))):
        for line in grid:
            line.insert(col_n, '.')

galaxies = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            galaxies.append((y, x))

result = 0
for p1,p2 in product(galaxies,repeat = 2):
    y1,x1=p1
    y2,x2=p2
    result += abs(y2-y1)+abs(x2-x1)


print(result//2)
print(time.time() - start_time)
