import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

states = [(-1, 0, 1, 0)]

reflections = {"/": {(1, 0): [(0, -1)], (-1, 0): [(0, 1)], (0, 1): [(-1, 0)], (0, -1): [(1, 0)]},
               '\\': {(1, 0): [(0, 1)], (-1, 0): [(0, -1)], (0, 1): [(1, 0)], (0, -1): [(-1, 0)]},
               '-': {(1, 0): [(1, 0)], (-1, 0): [(-1, 0)], (0, 1): [(-1, 0), (1, 0)], (0, -1): [(-1, 0), (1, 0)]},
               '|': {(1, 0): [(0, -1), (0, 1)], (-1, 0): [(0, -1), (0, 1)], (0, 1): [(0, 1)], (0, -1): [(0, -1)]}}

visited_counter = set()
state_counter = set()

while states:
    x, y, dx, dy = states.pop(0)

    if (x, y, dx, dy) not in state_counter:
        state_counter.add((x, y, dx, dy))
        visited_counter.add((x, y))
        nx = x + dx
        ny = y + dy

        if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
            new_space = lines[ny][nx]
            if new_space != '.':
                for ndx, ndy in reflections[new_space][(dx, dy)]:
                    states.append((nx, ny, ndx, ndy))
            else:
                states.append((nx, ny, dx, dy))

print(len(visited_counter) - 1)
print(time.time() - start_time)
