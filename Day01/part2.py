import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6',
          '7', '8', '9']
convertor = {d: str((i + 1) % 10) for i, d in enumerate(digits)}

print(convertor)
result = 0
for line in lines:

    numbers = []

    for template in digits:
        i = 0
        while i + len(template) - 1 < len(line):
            chars = line[i:i + len(template)]
            if chars == template:
                numbers.append((i, convertor[template]))
            i += 1
    numbers.sort()
    temp = int(numbers[0][1] + numbers[-1][1])
    result += temp

print(result)
print(time.time() - start_time)
