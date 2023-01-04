from collections import deque
import numpy as np

class Monkey:
    def __init__(self, items, op, test, if_t, if_f):
        self.items = deque(items)
        self.op = op
        self.test_val = test
        self.test = lambda x: x % test == 0
        self.if_t = if_t
        self.if_f = if_f
        self.inspections = 0

    def inspect(self):
        self.inspections += 1

#  monkeys = [
    #  Monkey(items=[79, 98], op=lambda x: 19*x, test=23, if_t=2, if_f=3),
    #  Monkey(items=[54, 65, 75, 74], op=lambda x: x + 6, test=19, if_t=2, if_f=0),
    #  Monkey(items=[79, 60, 97], op=lambda x: x*x, test=13, if_t=1, if_f=3),
    #  Monkey(items=[74], op=lambda x: x + 3, test=17, if_t=0, if_f=1)
#  ]

monkeys = [
    Monkey(items=[66, 71, 94], op=lambda x: 5*x, test=3, if_t=7, if_f=4),
    Monkey(items=[70], op=lambda x: x + 6, test=17, if_t=3, if_f=0),
    Monkey(items=[62, 68, 56, 65, 94, 78], op=lambda x: x + 5, test=2, if_t=3, if_f=1),
    Monkey(items=[89, 94, 94, 67], op=lambda x: x + 2, test=19, if_t=7, if_f=0),
    Monkey(items=[71, 61, 73, 65, 98, 98, 63], op=lambda x: 7*x, test=11, if_t=5, if_f=6),
    Monkey(items=[55, 62, 68, 61, 60], op=lambda x: x + 7, test=5, if_t=2, if_f=1),
    Monkey(items=[93, 91, 69, 64, 72, 89, 50, 71], op=lambda x: x + 1, test=13, if_t=5, if_f=2),
    Monkey(items=[76, 50], op=lambda x: x*x, test=7, if_t=4, if_f=6)
]

for _ in range(20):
    for m in monkeys:
        while m.items:
            item = m.items.popleft()
            item = m.op(item)
            m.inspect()
            item = item // 3

            to_monkey = m.if_t if m.test(item) else m.if_f
            monkeys[to_monkey].items.append(item)

insp = [m.inspections for m in monkeys]
top2 = sorted(insp)[-2:]
sol_a = top2[0]*top2[1]
print(f"A ::: {sol_a}")

monkeys = [
    Monkey(items=[66, 71, 94], op=lambda x: 5*x, test=3, if_t=7, if_f=4),
    Monkey(items=[70], op=lambda x: x + 6, test=17, if_t=3, if_f=0),
    Monkey(items=[62, 68, 56, 65, 94, 78], op=lambda x: x + 5, test=2, if_t=3, if_f=1),
    Monkey(items=[89, 94, 94, 67], op=lambda x: x + 2, test=19, if_t=7, if_f=0),
    Monkey(items=[71, 61, 73, 65, 98, 98, 63], op=lambda x: 7*x, test=11, if_t=5, if_f=6),
    Monkey(items=[55, 62, 68, 61, 60], op=lambda x: x + 7, test=5, if_t=2, if_f=1),
    Monkey(items=[93, 91, 69, 64, 72, 89, 50, 71], op=lambda x: x + 1, test=13, if_t=5, if_f=2),
    Monkey(items=[76, 50], op=lambda x: x*x, test=7, if_t=4, if_f=6)
]

CONST = np.prod([m.test_val for m in monkeys])

for _ in range(10_000):
    for m in monkeys:
        while m.items:
            item = m.items.popleft()
            item = m.op(item) % CONST
            m.inspect()

            to_monkey = m.if_t if m.test(item) else m.if_f
            monkeys[to_monkey].items.append(item)

insp = [m.inspections for m in monkeys]
top2 = sorted(insp)[-2:]
sol_b = top2[0]*top2[1]
print(f"B ::: {sol_b}")
