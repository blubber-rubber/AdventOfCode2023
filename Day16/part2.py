import time

from multiprocessing import Pool

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

reflections = {"/": {(1, 0): [(0, -1)], (-1, 0): [(0, 1)], (0, 1): [(-1, 0)], (0, -1): [(1, 0)]},
               '\\': {(1, 0): [(0, 1)], (-1, 0): [(0, -1)], (0, 1): [(1, 0)], (0, -1): [(-1, 0)]},
               '-': {(1, 0): [(1, 0)], (-1, 0): [(-1, 0)], (0, 1): [(-1, 0), (1, 0)], (0, -1): [(-1, 0), (1, 0)]},
               '|': {(1, 0): [(0, -1), (0, 1)], (-1, 0): [(0, -1), (0, 1)], (0, 1): [(0, 1)], (0, -1): [(0, -1)]}}


def get_n_energized_tiles(sx, sy, sdx, sdy):
    states = [(sx, sy, sdx, sdy)]

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
                if new_space in '\\/|-':
                    for ndx, ndy in reflections[new_space][(dx, dy)]:
                        states.append((nx, ny, ndx, ndy))
                else:
                    states.append((nx, ny, dx, dy))
    return len(visited_counter) - 1


if __name__ == '__main__':
    start_time = time.time()

    start_states = [(-1, row_n, 1, 0) for row_n in range(len(lines))] + \
                   [(len(lines[0]), row_n, -1, 0) for row_n in range(len(lines))] + \
                   [(col_n, -1, 0, 1) for col_n in range(len(lines))] + \
                   [(col_n, len(lines), 0, -1) for col_n in range(len(lines))]

    with Pool() as p:
        lijst = p.starmap(get_n_energized_tiles, start_states)
    print(max(lijst))
    print(time.time() - start_time)
