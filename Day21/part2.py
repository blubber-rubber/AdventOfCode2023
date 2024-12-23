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

STEPS = 26501365

SQUARE_LENGTH = len(grid)

n_full_squares_to_the_right = (STEPS - SQUARE_LENGTH) // SQUARE_LENGTH

n_odd_full_squares = (2 * (n_full_squares_to_the_right // 2) + 1) ** 2
n_even_full_squares = (2 * ((n_full_squares_to_the_right + 1) // 2)) ** 2

remaining_steps = STEPS % SQUARE_LENGTH + 2 * SQUARE_LENGTH
print(n_full_squares_to_the_right, n_odd_full_squares, n_even_full_squares, remaining_steps)


def get_neighbours(p, visited, grid):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighs = []
    cx, cy = p

    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy

        if (nx, ny) not in visited and grid[ny % SQUARE_LENGTH][nx % SQUARE_LENGTH] != '#':
            neighs.append((nx, ny))
    return neighs


visited = {start_position: 0}

current_positions = [(0, start_position)]
heapq.heapify(current_positions)

while current_positions:
    cd, cp = heapq.heappop(current_positions)
    if cd < remaining_steps:
        for p in get_neighbours(cp, visited, grid):
            visited[p] = cd + 1
            heapq.heappush(current_positions, (cd + 1, p))

ends_0 = {(-2, 0), (2, 0), (0, 2), (0, -2)}
diags_0 = {(1, 1), (1, -1), (-1, 1), (-1, -1)}
extra_0 = {(2, 1), (-2, 1), (-2, -1), (2, -1)}

all_evens = {k for k, v in visited.items() if v % 2 == 0}
all_odds = {k for k, v in visited.items() if v % 2 != 0}

diags = {k for k, v in visited.items() if (k[0] // SQUARE_LENGTH, k[1] // SQUARE_LENGTH) in diags_0}
ends = {k for k, v in visited.items() if (k[0] // SQUARE_LENGTH, k[1] // SQUARE_LENGTH) in ends_0}
extra = {k for k, v in visited.items() if (k[0] // SQUARE_LENGTH, k[1] // SQUARE_LENGTH) in extra_0}

full_square = {k for k, v in visited.items() if k[0] // SQUARE_LENGTH == 0 and k[1] // SQUARE_LENGTH == 0}

le = len(extra.intersection(all_odds))

result = 0

result += n_even_full_squares * len(full_square.intersection(all_evens))
result += n_odd_full_squares * len(full_square.intersection(all_odds))
result += len(ends.intersection(all_odds))
result += n_full_squares_to_the_right * len(diags.intersection(all_odds))
result += (n_full_squares_to_the_right + 1) * le

print(result)
print(time.time() - start_time)