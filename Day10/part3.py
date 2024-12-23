import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

grid = []

start = None

for y, line in enumerate(lines):
    lijn = [x for x in line]
    grid.append(lijn)
    if 'S' in lijn:
        start = (y, lijn.index('S'))

visited = set()
pipe_path = []

current_pos = start

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

connections = {'F': [(1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)], '7': [(1, 0), (0, -1)], 'L': [(-1, 0), (0, 1)],
               '-': [(0, -1), (0, 1)], '|': [(-1, 0), (1, 0)], 'S': dirs, '.': []}

while current_pos not in visited:
    visited.add(current_pos)
    pipe_path.append(current_pos)
    c_y, c_x = current_pos
    possible_connections = []

    old_pos_pipe = grid[c_y][c_x]

    for y_dir, x_dir in connections[old_pos_pipe]:
        y = c_y + y_dir
        x = x_dir + c_x

        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            new_pos_pipe = grid[y][x]

            for p_y, p_x in connections[new_pos_pipe]:
                if p_y + y_dir == 0 and p_x + x_dir == 0 and (y, x) not in visited:
                    possible_connections.append((y, x))

    if not possible_connections:
        current_pos = start
    else:
        current_pos = possible_connections[0]

new_grid = [['.'] * (len(grid[0]) * 2 + 1)]
old_positions = set()
for y in range(len(grid)):
    new_grid.append(['.'])
    new_grid.append(['.'])
    for x in range(len(grid[0])):
        new_grid[2 * y + 1].append(grid[y][x])
        new_grid[2 * y + 1].append('.')
        new_grid[2 * y + 2].append('.')
        new_grid[2 * y + 2].append('.')

        old_positions.add((2 * y + 1, 2 * x + 1))

visited1 = set()
for p1, p2 in zip(pipe_path, pipe_path[1:] + pipe_path[:1]):
    y1, x1 = p1
    y2, x2 = p2

    ny1 = 2 * y1 + 1
    ny2 = 2 * y2 + 1
    nx1 = 2 * x1 + 1
    nx2 = 2 * x2 + 1

    midx = (nx1 + nx2) // 2
    midy = (ny1 + ny2) // 2

    visited1.add((ny1, nx1))
    visited1.add((ny2, nx2))
    visited1.add((midy, midx))
    if ny1 == ny2:
        new_grid[midy][midx] = '-'
    else:
        new_grid[midy][midx] = '|'


def bfs_coloring(positions, coloring, color, grid):
    while positions:
        current_pos = positions.pop()
        coloring[current_pos] = color
        c_y, c_x = current_pos
        for d_y, d_x in dirs:
            n_y = c_y + d_y
            n_x = c_x + d_x

            if 0 <= n_y < len(grid) and 0 <= n_x < len(grid[0]) and (n_y, n_x) not in coloring:
                positions.append((n_y, n_x))


coloring = {p: 0 for p in visited1}
color = 1
for y in range(len(new_grid)):
    for x in range(len(new_grid[0])):
        if (y, x) not in coloring:
            bfs_coloring([(y, x)], coloring, color, new_grid)
            color += 1

outside_color = coloring[(len(new_grid) - 1, len(new_grid[0]) - 1)]

inside = [p for p in old_positions if coloring[p] not in [0, outside_color]]

print(len(inside))
print(time.time() - start_time)
