import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

inventory = set(int(x) for x in lines[0].split(':')[1].strip(' ').split(' '))

line_i = 3

while line_i < len(lines):
    line = lines[line_i]
    converter = {}
    new_inventory = set()
    old_inventory = inventory.copy()
    while line_i < len(lines) and lines[line_i] != '':
        line = lines[line_i]
        a, b, c = [int(x) for x in line.split(' ')]

        for source in old_inventory:
            if b <= source < b + c:
                inventory.remove(source)
                new_inventory.add(a+source-b)



        line_i += 1



    inventory = inventory.union(new_inventory)
    print('----')
    line_i += 2

print(min(inventory))
print(time.time() - start_time)
