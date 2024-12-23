import time
import sympy

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

hailstones = []

for line in lines:
    pos, velo = line.strip().split('@')

    pos = tuple(int(x) for x in pos.strip().split(', '))
    velo = tuple(int(x) for x in velo.strip().split(', '))

    hailstones.append((pos, velo))

n_hailstones = 3


def solve_equations(n_hailstones):
    x, y, z, vx, vy, vz, = sympy.symbols("x y z vx vy vz", real=True)

    ks = []
    for i in range(n_hailstones):
        ks.append(sympy.symbols(f"k{i + 1}", real=True))


    eqs = []
    for i in range(n_hailstones):
        k = ks[i]
        p, v = hailstones[i]

        eqs.append(sympy.Eq(x + k * vx - p[0] - k * v[0], 0))
        eqs.append(sympy.Eq(y + k * vy - p[1] - k * v[1], 0))
        eqs.append(sympy.Eq(z + k * vz - p[2] - k * v[2], 0))

    sol = sympy.solve(eqs)[0]
    return sol[x]+sol[y]+sol[z]


print(solve_equations(3))
print(time.time() - start_time)
