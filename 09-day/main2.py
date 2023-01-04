import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lines = open('input.txt', 'r').readlines()

#  lines = """R 4
#  U 4
#  L 3
#  D 1
#  R 4
#  D 1
#  L 5
#  R 2""".strip().split('\n')

#  lines = """R 5
#  U 8
#  L 8
#  D 3
#  R 17
#  D 10
#  L 25
#  U 20""".strip().split('\n')

moves = [(l.split()[0], int(l.strip().split()[1])) for l in lines]

class Knot:
    def __init__(self, lbl=None):
        self.lbl = lbl
        self.x, self.y = 0, 0
        self.history = [(0, 0)]
        self.last_move = ''
        self.child = None
        self.parent = None

    def __repr__(self):
        return f"Knot({self.lbl}, {self.x}, {self.y})"

    def move(self, d=None):
        if not d:

            dx = self.parent.x - self.x
            dy = self.parent.y - self.y

            # Move when child
            if dx == 2:
                self.x += 1
                if dy == 1:
                    self.y += 1
                elif dy == -1:
                    self.y -= 1
            elif dx == -2:
                self.x -= 1
                if dy == 1:
                    self.y += 1
                elif dy == -1:
                    self.y -= 1
            elif dy == 2:
                self.y += 1
                if dx == 1:
                    self.x += 1
                elif dx == -1:
                    self.x -= 1
            elif dy == -2:
                self.y -= 1
                if dx == 1:
                    self.x += 1
                elif dx == -1:
                    self.x -= 1

        # Move when given explicit direction
        else:
            if d == 'U':
                self.y += 1
            elif d == 'R':
                self.x += 1
            elif d == 'L':
                self.x -= 1
            elif d == 'D':
                self.y -= 1

        self.history.append((self.x, self.y))
        
        if self.child:
            self.child.move()

    def plot_history(self):
        df = pd.DataFrame(self.history, columns=['x', 'y']).drop_duplicates()
        df.plot(kind='scatter', x='x', y='y')
        plt.show()

h = Knot()
t = Knot()

h.child = t
t.parent = h

for d, n in moves:
    for _ in range(n):
        h.move(d)

hist = pd.DataFrame(t.history).drop_duplicates()
print(f"A ::: {hist.shape[0]}")

chain = [Knot(lbl=i) for i in range(10)]
for i in range(9):
    chain[i].child = chain[i + 1]
for i in range(1, 10):
    chain[i].parent = chain[i - 1]

for d, n in moves:
    for _ in range(n):
        chain[0].move(d)

t = chain[-1]
hist = pd.DataFrame(t.history).drop_duplicates()

# 2084 too low
# 2805 too high
print(f"B ::: {hist.shape[0]}")
