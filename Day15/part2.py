import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


def get_hash(part):
    current_value = 0

    for ch in part:
        current_value += ord(ch)
        current_value *= 17
        current_value = current_value % 256

    return current_value


boxes = defaultdict(list)
result = 0

for part in lines[0].split(','):
    if '=' in part:
        a, b = part.split('=')


        relevant_box = boxes[get_hash(a)]
        i = len(relevant_box) - 1
        replacement = []
        while i >= 0:
            if relevant_box[i][0] == a:
                replacement.append(i)
            i -= 1

        if replacement:
            for r in replacement:
                relevant_box[r] = (a, int(b))
        else:
            relevant_box.append((a, int(b)))
    else:
        part = part[:-1]

        relevant_box = boxes[get_hash(part)]

        i = len(relevant_box) - 1

        while i >= 0:
            if relevant_box[i][0] == part:
                del relevant_box[i]
            i -= 1



result = 0

for key, box in boxes.items():
    for i, lens in enumerate(box):
        result += (key + 1) * (i + 1) * lens[1]

print(result)

print(time.time() - start_time)
