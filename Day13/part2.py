import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

index = 0


def transpose(grid):
    return [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]


test = transpose([['a', 'b'], ['c', 'd']])
result = 0
while index < len(lines):
    grid = []

    while index < len(lines) and lines[index] != '':
        grid.append([x for x in lines[index]])
        index += 1

    pos_cols = set(range(0, len(grid[0]) - 1))
    bad_cols = defaultdict(int)
    searching = True
    for row in grid:
        for col in pos_cols:
            for d in range(min(col + 1, len(row) - 1 - col)):
                if row[col - d] != row[col + 1 + d]:
                    bad_cols[col] += 1

    t_grid = transpose(grid)
    pos_rows = set(range(0, len(t_grid[0]) - 1))
    bad_rows = defaultdict(int)
    searching = True
    for col in t_grid:
        for row in pos_rows:
            for d in range(min(row + 1, len(col) - 1 - row)):
                if col[row - d] != col[row + 1 + d]:
                    bad_rows[row] += 1

    mirror_cols = set(k for k, v in bad_cols.items() if v == 1)
    mirror_rows = set(k for k, v in bad_rows.items() if v == 1)

    mirrors = list(mirror_rows.union(mirror_cols))

    if len(mirrors) != 1:
        print('help')

    if mirror_cols:
        for x in mirror_cols:
            result += x + 1
    else:
        for x in mirror_rows:
            result += 100 * (x + 1)

    index += 1

print(result)
print(time.time() - start_time)
