import time
from functools import cache
import heapq

start_time = time.time()

with open('input.txt') as f:
    grid = [[int(x) for x in line.rstrip('\n')] for line in f.readlines()]


@cache
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] + p2[1])


def get_neighbours(s, score, grid):
    cp, dir, n_dir = s
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    neighs = {}
    cx, cy = cp

    for dx, dy in dirs:

        if (dir is None) or ((dx, dy) != dir and (dir[0] + dx != 0 or dir[1] + dy != 0)):
            k = 0
            nx = cx
            ny = cy
            ns = score
            while k < 10:
                nx += dx
                ny += dy
                k += 1

                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    ns += grid[ny][nx]
                    if k >= 4:
                        neighs[((nx, ny), (dx, dy), k,)] = ns

    return neighs


def a_star(start, end, neighbours, heuristic, grid):
    positions = [(0 + heuristic(start, end), (start, None, 0))]
    heapq.heapify(positions)

    visited = {p for hs, p in positions}
    min_sols = []

    while not min_sols or (min_sols and positions[0][0] < min(min_sols)):
        hs, current_state = heapq.heappop(positions)

        neighbours_dict = neighbours(current_state, hs - heuristic(end, current_state[0]), grid)
        for p in neighbours_dict:
            if p not in visited:
                visited.add(p)
                heapq.heappush(positions, (neighbours_dict[p] + heuristic(end, p[0]), p))
                if p[0] == end:
                    min_sols.append(neighbours_dict[p])

    print(min_sols)
    return min(min_sols)


start = (0, 0)
end = (len(grid[0]) - 1, len(grid) - 1)

print(a_star(start, end, get_neighbours, manhattan_distance, grid))
print(time.time() - start_time)
