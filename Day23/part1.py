import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

grid = [[x for x in line] for line in lines]

DIRECTIONS = {'<': [(-1, 0)], '>': [(1, 0)], '^': [(0, -1)], 'v': [(0, 1)], '.': [(0, 1), (0, -1), (1, 0), (-1, 0)]}

destination = (len(grid[0]) - 2, len(grid) - 1)

crossroads = [(1, 0), destination]

graph = defaultdict(dict)

for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] == '.':
            possible_outways = [(x + dx, y + dy) for dx, dy in DIRECTIONS[grid[y][x]] if grid[y + dy][x + dx] != '#']

            if len(possible_outways) > 2:
                crossroads.append((x, y))


def get_neighbours(p, grid, current_visited):
    neighs = []
    cx, cy = p

    for dx, dy in DIRECTIONS[grid[cy][cx]]:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != '#' and (nx, ny) not in current_visited:
            neighs.append((nx, ny))
    return neighs


def get_next_crossroads(p, crossroads, graph):
    start_states = [(0, p[0], p[1], set())]

    while start_states:
        current_distance, cx, cy, current_visited = start_states.pop()
        current_visited.add((cx, cy))

        if (cx, cy) != p and (cx, cy) in crossroads:
            graph[p][(cx, cy)] = (current_distance, current_visited.copy())

        else:
            for nx, ny in get_neighbours((cx, cy), grid, current_visited):
                start_states.append((current_distance + 1, nx, ny, current_visited.copy()))


for c in crossroads:
    get_next_crossroads(c, crossroads, graph)

start_states = [(0, (1, 0), set())]
longest_distance = 0

while start_states:
    current_distance, p, current_visited = start_states.pop()
    current_visited.add(p)

    if p == destination:
        longest_distance = max(longest_distance, current_distance)


    else:
        new_crossroads = graph[p]
        if destination in new_crossroads:
            new_crossroads = [destination]
        for new_crossroad in new_crossroads:

            dist, used_spaces = graph[p][new_crossroad]

            if new_crossroad not in current_visited:
                start_states.append((current_distance + dist, new_crossroad, current_visited.copy()))


print(longest_distance)
print(time.time() - start_time)
