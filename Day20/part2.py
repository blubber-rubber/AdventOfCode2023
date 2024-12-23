import time
from collections import defaultdict

start_time = time.time()

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


class Module:
    def __init__(self):
        self.name = None
        self.previous_modules = []
        self.next_modules = []
        self.t = 'm'

    def add_prev_mod(self, mod):
        self.previous_modules.append(mod)

    def add_next_mod(self, mod):
        self.next_modules.append(mod)

    def receive_signal(self, prev_mod, signal):
        return []

    def set_name(self, name):
        self.name = name


class FlipFlopModule:

    def __init__(self):
        self.name = None
        self.previous_modules = []
        self.next_modules = []
        self.state = False
        self.t = 'flipflop'

    def add_prev_mod(self, mod):
        self.previous_modules.append(mod)

    def add_next_mod(self, mod):
        self.next_modules.append(mod)

    def receive_signal(self, prev_mod, signal):
        if signal == 'l':
            self.state = not self.state

            new_s = 'h' if self.state else 'l'

            return [] + [(self.name, dest, new_s) for dest in self.next_modules]

    def set_name(self, name):
        self.name = name


class ConjucnctionModule:

    def __init__(self):
        self.name = None
        self.previous_modules = dict()
        self.next_modules = []
        self.t = 'conj'

    def add_prev_mod(self, mod):
        self.previous_modules[mod] = False

    def add_next_mod(self, mod):
        self.next_modules.append(mod)

    def receive_signal(self, prev_mod, signal):
        self.previous_modules[prev_mod] = False if signal == 'l' else True
        new_s = 'l' if all(x for x in self.previous_modules.values()) else 'h'
        return [] + [(self.name, dest, new_s) for dest in self.next_modules]

    def set_name(self, name):
        self.name = name


class BroadcastModule:

    def __init__(self):
        self.name = 'broadcaster'
        self.previous_modules = []
        self.next_modules = []
        self.t = 'broadcaster'

    def add_prev_mod(self, mod):
        self.previous_modules.append(mod)

    def add_next_mod(self, mod):
        self.next_modules.append(mod)

    def receive_signal(self, prev_mod, signal):
        return [] + [(self.name, dest, signal) for dest in self.next_modules]

    def set_name(self, name):
        self.name = name


class ButtonModule:

    def __init__(self):
        self.name = 'button'
        self.previous_modules = []
        self.next_modules = []
        self.t = 'button'

    def add_prev_mod(self, mod):
        self.previous_modules.append(mod)

    def add_next_mod(self, mod):
        self.next_modules.append(mod)

    def receive_signal(self, prev_mod, signal):
        return [] + [(self.name, dest, 'l') for dest in self.next_modules]

    def set_name(self, name):
        self.name = name


modules = dict()

for line in lines:
    source, dests = line.split(' -> ')

    if source != 'broadcaster':
        if source[0] == '%':
            modules[source[1:]] = FlipFlopModule()
        else:
            modules[source[1:]] = ConjucnctionModule()
    else:
        modules[source] = BroadcastModule()

modules['button'] = ButtonModule()

for line in lines:
    source, dests = line.split(' -> ')
    if source != 'broadcaster':
        source = source[1:]
    for d in dests.split(', '):
        if d not in modules:
            modules[d] = Module()

        modules[source].add_next_mod(d)
        modules[d].add_prev_mod(source)

        modules[source].set_name(source)
        modules[d].set_name(d)

modules['button'].add_next_mod('broadcaster')
modules['broadcaster'].add_prev_mod('button')

low_pulses = 0
high_pulses = 0
heap = []
N = 1000

rx_counter = 0
button_presses = 0
while rx_counter ==0:
    button_presses += 1
    heap = [('button', 'broadcaster', 'l')]

    while heap:
        prev_module_name, current_module_name, signal = heap.pop(0)



        if current_module_name  == 'cs' and signal == 'h':
            print(button_presses)
            print(f'{prev_module_name} -{signal}-> {current_module_name}')
            #rx_counter += 1
        current_module = modules[current_module_name]

        new_signals = current_module.receive_signal(prev_module_name, signal)
        if new_signals is not None:
            heap += new_signals

    if button_presses%1000000 == 0:
        print(button_presses)
    # for m in modules.values():
    #     if m.t == 'flipflop':
    #         print(m.name, m.state, m.previous_modules)
    #     elif m.t == 'conj':
    #         print(m.name, m.previous_modules)
    #
    # print('-------')
    #print(modules['fm'].state)

print(button_presses)

print(time.time() - start_time)
