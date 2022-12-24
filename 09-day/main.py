import pandas as pd

lines = open('input.txt', 'r').readlines()

#  lines = """R 4
#  U 4
#  L 3
#  D 1
#  R 4
#  D 1
#  L 5
#  R 2""".strip().split('\n')

moves = [(l.split()[0], int(l.strip().split()[1])) for l in lines]

class Knot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.history = [(0, 0)]
        self.last_move = ''

    def move(self, d):
        if d == 'U':
            self.y += 1
        elif d == 'R':
            self.x += 1
        elif d == 'L':
            self.x -= 1
        elif d == 'D':
            self.y -= 1

        self.history.append((self.x, self.y))
        self.last_move = d

    def assign(self, x, y):
        self.x, self.y = x, y
        self.history.append((self.x, self.y))

def is_far(p, q):
    return abs(p.x - q.x) > 1 or abs(p.y - q.y) > 1

h = Knot()
t = Knot()

for d, n in moves:
    for _ in range(n):
        h.move(d)
        if is_far(t, h):
            if d == 'U':
                t.assign(h.x, h.y - 1)
            elif d == 'R':
                t.assign(h.x - 1, h.y)
            elif d == 'L':
                t.assign(h.x + 1, h.y)
            elif d == 'D':
                t.assign(h.x, h.y + 1)

hist = pd.DataFrame(t.history).drop_duplicates()
print(hist.shape[0])
