import time
import heapq

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

grid = [[x for x in line] for line in lines]

for y in range(len(lines)):
    for x in range(len(lines[0])):

        if grid[y][x] == 'S':
            start_position = (x, y)

STEPS = 64


def get_neighbours(p, visited, grid):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighs = []
    cx, cy = p

    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[ny][nx] != '#':
            neighs.append((nx, ny))
    return neighs


visited = {start_position: 0}

current_positions = [(0, start_position)]
heapq.heapify(current_positions)

while current_positions:
    cd, cp = heapq.heappop(current_positions)
    if cd < STEPS:
        for p in get_neighbours(cp, visited, grid):
            visited[p] = cd + 1
            heapq.heappush(current_positions, (cd + 1, p))

gp = [k for k, v in visited.items() if v % 2 == 1 and v <= STEPS]
print(len(gp))

print(time.time() - start_time)
