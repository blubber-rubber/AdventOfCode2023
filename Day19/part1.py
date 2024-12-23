import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


class Checker():

    def __init__(self):
        self.conditions = None
        self.default = None

    def set_meta(self, conds, default):
        self.conditions = conds
        self.default = default

    def check(self, check_object):

        destination_map = []
        for cond, dest in self.conditions:

            if check_object is not None:

                if '<' in cond:

                    og_copy = check_object.copy()
                    a, b = cond.split('<')

                    prop_range = check_object[a]

                    min_prop, max_prop = prop_range

                    if min_prop < int(b):
                        og_copy[a] = (min_prop, min(int(b), max_prop))
                        destination_map.append((og_copy, dest))
                        if max_prop < int(b):
                            check_object = None
                        else:
                            check_object[a] = (int(b), max_prop)

                else:
                    og_copy = check_object.copy()
                    a, b = cond.split('>')

                    prop_range = check_object[a]

                    min_prop, max_prop = prop_range

                    if max_prop > int(b):
                        og_copy[a] = (max(int(b), min_prop), max_prop)
                        destination_map.append((og_copy, dest))
                        if min_prop > int(b):
                            check_object = None
                        else:
                            check_object[a] = (min_prop, int(b))

        if check_object is not None:
            destination_map.append((check_object, self.default))

        return destination_map


workflows = defaultdict(lambda: Checker())

i = 0

while lines[i] != '':
    line = lines[i]
    i += 1

    name, conds = line[:-1].split('{')
    conditions = []
    condition_strings = conds.split(',')

    for condition in condition_strings[:-1]:
        cond, dest = condition.split(':')

        conditions.append((cond, dest))

    default = condition_strings[-1]

    checker = workflows[name]

    checker.set_meta(conditions, default)

result = 0

check_objects = [({p: (1, 4000) for p in ['x', 'm', 'a', 's']}, 'in')]

while check_objects:
    check_object, check_s = check_objects.pop()
    checker = workflows[check_s]

    new_check_objects = checker.check(check_object)

    for nco in new_check_objects:
        ob, dest = nco

        if dest == 'A':
            pass
        elif dest != 'R':
            check_objects.append(nco)

i += 1

print(result)
print(time.time() - start_time)
