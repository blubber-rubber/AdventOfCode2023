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
    for x_start in range(MAX_X):
        if lines[y_start][x_start] == '*':
            neighbours = []
            for dx, dy in delta:
                x = x_start + dx
                y = y_start + dy

                if 0 <= x < MAX_X and 0 <= y < MAX_Y and lines[y][x] in '0123456789':
                    neighbours.append((y, x))

            final = []
            i1, i2 = 0, 0
            while not final and i1 < len(neighbours):
                n1 = neighbours[i1]
                y1, x1 = n1
                while not final and i2 < len(neighbours):
                    n2 = neighbours[i2]
                    y2, x2 = n2

                    if (y1 != y2) or (y1 == y2 and abs(x1 - x2) > 1 and lines[y1][(x1 + x2) // 2] not in '0123456789'):
                        final = [n1, n2]

                    i2 += 1
                i1 += 1
            if final:
                temp_result = 1
                for y, x in final:
                    for match in re.finditer('[0-9][0-9]*', lines[y]):
                        start_x = match.start()
                        end_x = match.end()
                        if start_x <= x < end_x:
                            temp_result *= int(match.group())

                result += temp_result

print(result)
print(time.time() - start_time)
