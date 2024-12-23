import time
import math

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

current_nodes = [nodes[key] for key in nodes.keys() if key[-1] == 'A']

result = 0

cycle_info = []

cycle_lengths = []

for current_node in current_nodes:
    zs = set()
    visited = {}
    instr_i = 0
    while current_node.name not in visited or (instr_i - visited[current_node.name]) % len(instructions) != 0:
        if current_node.name[-1] == "Z":
            zs.add(instr_i)
        visited[current_node.name] = instr_i
        instr = instructions[instr_i % len(instructions)]
        instr_i += 1
        if instr == 'L':
            current_node = nodes[current_node.left]
        else:
            current_node = nodes[current_node.right]

    cycle_info.append([z for z in zs if z >= visited[current_node.name]])
    cycle_length = instr_i - visited[current_node.name]
    cycle_lengths.append(cycle_length)



# result = 0
# while any(current_node.name[-1] != 'Z' for current_node in current_nodes) and result <= max(cycle_lengths):
#
#     instr = instructions[result % len(instructions)]
#     result += 1
#     if instr == 'L':
#         current_nodes = [nodes[current_node.left] for current_node in current_nodes]
#     else:
#         current_nodes = [nodes[current_node.right] for current_node in current_nodes]
#
# i_s = [0] * len(cycle_info)
#
# while not set.intersection(
#         *[set(info + i_s[i] * cycle_lengths[i] for info in cycle_info[i]) for i in range(len(cycle_lengths))]):
#     min_i = min(range(len(cycle_lengths)), key=lambda x: min(cycle_info[x]) + i_s[x] * cycle_lengths[x])
#     i_s[min_i] += 1
#
# print('d')

print(math.lcm(*cycle_lengths))
print(time.time() - start_time)
