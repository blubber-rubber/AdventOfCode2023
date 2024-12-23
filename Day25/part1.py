import time
from collections import defaultdict
from itertools import combinations

from tqdm import tqdm

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

connections = defaultdict(list)
for line in lines:
    s, cs = line.strip().split(':')

    for c in cs.strip().split(' '):
        connections[c].append(s)
        connections[s].append(c)

visited_counter = defaultdict(int)
for comp in tqdm(connections.keys()):
    current_paths = [[comp]]
    visited = {comp}
    while current_paths:
        cp = current_paths.pop(0)

        for next_comp in connections[cp[-1]]:
            if next_comp not in visited:
                path_copy = cp.copy()
                path_copy.append(next_comp)
                visited.add(next_comp)
                current_paths.append(path_copy)

                for p1, p2 in zip(path_copy, path_copy[1:]):
                    visited_counter[(p1, p2)] += 1
                    visited_counter[(p2, p1)] += 1
counter_lijst = [(k, v) for k, v in visited_counter.items()]
counter_lijst.sort(key=lambda x: x[1], reverse=True)


c1, c2, c3 = [x[0] for x in counter_lijst[:6:2]]
k1, v1 = c1
k2, v2 = c2
k3, v3 = c3

connections[k1].remove(v1)
connections[v1].remove(k1)
connections[k2].remove(v2)
connections[v2].remove(k2)
connections[k3].remove(v3)
connections[v3].remove(k3)

colors = dict()

color = 0
for part in connections.keys():
    if part not in colors:
        heap = [part]

        while heap:
            current = heap.pop()
            colors[current] = color

            for new_part in connections[current]:
                if new_part not in colors:
                    heap.append(new_part)

        color += 1

g1 = [c for c, v in colors.items() if v == 0]
g2 = [c for c, v in colors.items() if v == 1]
print(len(g1) * len(g2))
