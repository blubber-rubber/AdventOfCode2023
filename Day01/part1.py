import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


result = 0
for line in lines:

    numbers = []

    for char in line:
        if char in '1234567890':
            numbers.append(char)
    temp = int(numbers[0]+numbers[-1])
    result += temp

print(result)
print(time.time() - start_time)
