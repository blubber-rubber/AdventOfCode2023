import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

grid = [[0] * len(lines[0])]

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

current_pos = (0, 0)

coloring = {p: 0 for p in visited}


def bfs_coloring(positions, coloring, color):
    while positions:
        current_pos = positions.pop()
        coloring[current_pos] = color
        c_y, c_x = current_pos
        for d_y, d_x in dirs:
            n_y = c_y + d_y
            n_x = c_x + d_x

            if 0 <= n_y < len(grid) and 0 <= n_x < len(grid[0]) and (n_y, n_x) not in coloring:
                positions.append((n_y, n_x))


color = 1
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (y, x) not in coloring:
            bfs_coloring([(y, x)], coloring, color)
            color += 1

colors = set(coloring.values())

colors.remove(0)

left_colors = set()
right_colors = set()


def rotate_left(direct):
    return (-direct[1], direct[0])


i = 0
while colors and i + 1 < len(pipe_path):
    p1 = pipe_path[i]
    p2 = pipe_path[i + 1]
    y1, x1 = p1
    y2, x2 = p2

    current_dir = (y2 - y1, x2 - x1)
    rotated_dir = rotate_left(current_dir)

    buiten_pos = (y1 + rotated_dir[0], x1 + rotated_dir[1])
    if 0 <= buiten_pos[0] < len(grid) and 0 <= buiten_pos[1] < len(grid[1]):
        color = coloring[buiten_pos]
        if color in colors:
            colors.remove(color)
            left_colors.add(color)

    buiten_pos = (y2 + rotated_dir[0], x2 + rotated_dir[1])
    if 0 <= buiten_pos[0] < len(grid) and 0 <= buiten_pos[1] < len(grid[1]):
        color = coloring[buiten_pos]
        if color in colors:
            colors.remove(color)
            left_colors.add(color)

    rotated_dir = rotate_left(rotate_left(rotated_dir))

    buiten_pos = (y1 + rotated_dir[0], x1 + rotated_dir[1])
    if 0 <= buiten_pos[0] < len(grid) and 0 <= buiten_pos[1] < len(grid[1]):
        color = coloring[buiten_pos]
        if color in colors:
            colors.remove(color)
            right_colors.add(color)

    buiten_pos = (y2 + rotated_dir[0], x2 + rotated_dir[1])
    if 0 <= buiten_pos[0] < len(grid) and 0 <= buiten_pos[1] < len(grid[1]):
        color = coloring[buiten_pos]
        if color in colors:
            colors.remove(color)
            right_colors.add(color)
    i += 1

right_side = [k for k, v in coloring.items() if v in right_colors]
left_side = [k for k, v in coloring.items() if v in left_colors]
pipe = [k for k, v in coloring.items() if v == 0]

an_outside_color = coloring[(0, 0)]

if an_outside_color in right_colors:
    print(len(left_side))
else:
    print(len(right_side))

print(time.time() - start_time)
