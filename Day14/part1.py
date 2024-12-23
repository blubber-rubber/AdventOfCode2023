import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

columns = [[line[r] for line in lines] for r in range(len(lines[0]))]

tilted = []

result = 0

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

    weights = [x for i, x in enumerate(reversed(range(1, len(new_col) + 1))) if new_col[i] == 'O']

    result += sum(weights)

print(result)
print(time.time() - start_time)
