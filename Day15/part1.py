import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

result = 0

for part in lines[0].split(','):
    current_value = 0
    for ch in part:
        current_value += ord(ch)
        current_value *= 17
        current_value = current_value % 256

    result += current_value

print(result)

print(time.time() - start_time)
