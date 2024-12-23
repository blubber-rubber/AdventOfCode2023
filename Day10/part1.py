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



print(len(pipe_path)//2)

print(time.time() - start_time)
