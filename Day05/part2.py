import time

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

fline = [int(x) for x in lines[0].split(':')[1].strip(' ').split(' ')]

pairs = list(zip(fline[::2], fline[1::2]))

inventory = [(p[0], p[0] + p[1] - 1) for p in pairs]

line_i = 3

while line_i < len(lines):
    inventory.sort()
    line = lines[line_i]
    converter = {}

    converter = {}

    while line_i < len(lines) and lines[line_i] != '':
        line = lines[line_i]
        a, b, c = [int(x) for x in line.split(' ')]

        converter[(b, b + c - 1)] = a - b

        line_i += 1

    converter_keys = list(converter.keys())

    converter_keys.sort()

    inv_i = 0
    new_inventory = []
    while inv_i < len(inventory):
        range_done = False
        ran_s, ran_e = inventory[inv_i]
        key_i = 0
        while key_i < len(converter_keys) and converter_keys[key_i][1] < ran_s:
            key_i += 1
        if key_i < len(converter_keys):

            key_s, key_e = converter_keys[key_i]
            if not key_s > ran_e:
                overlap_s = max(ran_s, key_s)
                overlap_e = min(ran_e, key_e)

                if overlap_s > ran_s:
                    new_inventory.append((ran_s, overlap_s - 1))

                new_inventory.append((converter[(key_s, key_e)]+overlap_s, converter[(key_s, key_e)]+overlap_e))

                if overlap_e < ran_e:
                    inventory[inv_i] = (overlap_e + 1, ran_e)
                else:
                    inv_i += 1

            else:
                new_inventory.append((ran_s, ran_e))
                inv_i += 1
        else:
            new_inventory.append((ran_s, ran_e))
            inv_i += 1

    inventory = new_inventory
    print('----')
    line_i += 2

inventory.sort()
print(inventory[0][0])
print(time.time() - start_time)
