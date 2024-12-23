import time
from functools import lru_cache


start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


@lru_cache(maxsize=None)
def recursive_solve(cs, info):
    if not info:
        return 1
    total_teller = 0
    ci = max(range(len(info)), key=lambda x: info[x])
    l = info[ci]
    prev_sum = sum(info[:ci]) + ci
    next_sum = len(cs) - (sum(info[ci + 1:]) + len(info[ci + 1:]) + l)

    for i in range(prev_sum, next_sum + 1):
        if (i - 1 < 0 or cs[i - 1] in '.?') and (i + l >= len(cs) or cs[i + l] in '.?'):
            if all(cs[i + d] in '?#' for d in range(l)):
                current_sol = [x for x in cs]
                current_sol[i:i + l] = '#' * l

                if i - 1 >= 0:
                    current_sol[i - 1] = '.'

                if i + l < len(cs):
                    current_sol[i + l] = '.'

                lower_part = ''.join(current_sol[:i]).strip('.')
                upper_part = ''.join(current_sol[i + l:]).strip('.')

                lower_info = info[:ci]
                upper_info = info[ci + 1:]

                teller = 1

                upper_pos = True

                if not upper_info:
                    upper_pos = all(x in '?.' for x in upper_part)

                lower_pos = True
                if not lower_info:
                    lower_pos = all(x in '?.' for x in lower_part)

                teller *= upper_pos * lower_pos
                if upper_pos and lower_pos:
                    teller *= recursive_solve(lower_part, lower_info)
                    teller *= recursive_solve(upper_part, upper_info)

                total_teller += teller

    return total_teller


result = 0
for line in lines:
    teller = 0
    line, info = line.split(' ')

    line = "?".join(line for _ in range(5))
    info = ','.join(info for _ in range(5))

    line = line.strip('.')

    info = tuple(int(x) for x in info.split(','))
    temp = recursive_solve(line, info)

    result += temp

print(result)
print(time.time() - start_time)
