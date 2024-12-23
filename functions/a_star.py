import time
from functools import cache

start_time = time.time()

FAV_NUM = 1358

start = (1, 1)

end = (90, 90)


@cache
def is_open(x, y):
    return sum([int(x) for x in str(bin(x * x + 3 * x + 2 * x * y + y + y * y + FAV_NUM))[2:]]) % 2 == 0


@cache
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] + p2[0])


@cache
def euclid_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] + p2[0]) ** 2) ** .5


def get_neighbours(p):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighs = []
    cx, cy = p

    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy

        if nx >= 0 and ny >= 0 and is_open(nx, ny):
            neighs.append((nx, ny))
    return neighs


def a_star(start, end, neighbours, heuristic):
    visited = {start: 0}
    positions = [start]

    chain = {start: None}
    while end not in visited:
        positions.sort(key=lambda x: visited[x] + heuristic(x, end))
        current_pos = positions.pop(0)
        for p in neighbours(current_pos):

            if p not in visited:
                visited[p] = visited[current_pos] + 1
                chain[p] = current_pos
                positions.append(p)

    return visited, chain


visited, chain = a_star(start, end, get_neighbours, euclid_distance)
print(visited[end])
print(time.time() - start_time)
