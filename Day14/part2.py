import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

columns = [[line[r] for line in lines] for r in range(len(lines[0]))]


def rotate_cw(grid):
    return [[col[i] for col in grid] for i in reversed(range(len(grid[0])))]


def tilt(columns):
    new_columns = []
    for col in columns:
        index = 0
        new_col = []
        while index < len(col):
            start = index
            while index < len(col) and col[index] == '#':
                index += 1

            new_col += ["#"] * (index - start)
            start = index
            teller = 0
            while index < len(col) and col[index] != '#':
                if col[index] == 'O':
                    teller += 1
                index += 1

            new_col += ['O'] * teller + ['.'] * (index - start - teller)

        new_columns.append(new_col)
    return new_columns


def cycle(columns):
    for _ in range(4):
        columns = tilt(columns)
        columns = rotate_cw(columns)

    return columns


cycle_i = 0
cur_cycle = ''.join([''.join([x for x in col]) for col in columns])

cycles = {}

M = 1000000000

while cycle_i < M and cur_cycle not in cycles:
    cycles[cur_cycle] = cycle_i
    columns = cycle(columns)
    cur_cycle = ''.join([''.join([x for x in col]) for col in columns])
    cycle_i += 1

period = cycle_i - cycles[cur_cycle]

cycle_i += (((M - cycles[cur_cycle]) // period) - 1) * period

while cycle_i < M:
    cycles[cur_cycle] = cycle_i
    columns = cycle(columns)
    cur_cycle = ''.join([''.join([x for x in col]) for col in columns])
    cycle_i += 1


def get_weight(columns):
    result = 0
    for col in columns:
        weights = [x for i, x in enumerate(reversed(range(1, len(col) + 1))) if col[i] == 'O']

        result += sum(weights)
    return result


print(get_weight(columns))
print(time.time() - start_time)
