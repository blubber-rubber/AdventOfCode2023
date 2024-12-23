import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

instructions = lines[0]


class Node:

    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


nodes = {}

for line in lines[2:]:
    name, kids = line.split(' = ')
    l, r = kids.strip('()').split(', ')
    nodes[name] = Node(name, l, r)

current_node = nodes['AAA']

result = 0

while current_node.name != 'ZZZ':
    instr = instructions[result % len(instructions)]
    result += 1
    if instr == 'L':
        current_node = nodes[current_node.left]
    else:
        current_node = nodes[current_node.right]

print(result)
print(time.time() - start_time)
