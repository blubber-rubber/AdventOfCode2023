import time
import re

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]
MAX_Y = len(lines)
MAX_X = len(lines[0])

delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def is_symbol(x):
    return x != '.' and x not in '0123456789'


def get_neighbours(y_start, start_x, end_x):
    neighbours = [(y_start - 1, start_x - 1), (y_start, start_x - 1), (y_start + 1, start_x - 1), (y_start - 1, end_x),
                  (y_start, end_x), (y_start + 1, end_x)]

    for x in range(start_x, end_x):
        neighbours += [(y_start - 1, x), (y_start + 1, x)]

    return [n for n in neighbours if 0 <= n[0] < MAX_X and 0 <= n[1] < MAX_Y]


result = 0
for y_start, line in enumerate(lines):

    for match in re.finditer('[0-9][0-9]*', line):
        start_x = match.start()
        end_x = match.end()
        neighbours = get_neighbours(y_start, start_x, end_x)

        if any(lines[y][x] != '.' for y, x in neighbours):
            result += int(match.group())

#     for x_start in range(max_x):
#         for dx, dy in delta:
#             if lines[]
#
#             x = x_start + dx
#             y = y_start + dy
#
#             if 0 <= x < max_x and 0 <= y < max_y and lines[y][x] in '0123456789':
#                 result += int(lines[y][x])
#
print(result)
print(time.time() - start_time)
