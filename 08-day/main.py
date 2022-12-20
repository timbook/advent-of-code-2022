import numpy as np
from itertools import product

import pdb

lines = open('input.txt', 'r').readlines()
grid = np.array([list(line.strip()) for line in lines]).astype(int)

#  grid = np.array([
    #  [3, 0, 3, 7, 3],
    #  [2, 5, 5, 1, 2],
    #  [6, 5, 3, 3, 2],
    #  [3, 3, 5, 4, 9],
    #  [3, 5, 3, 9, 0]
#  ])

nrow, ncol = grid.shape

count = 0
for r, c in product(range(1, nrow - 1), range(1, ncol - 1)):
    row = grid[r, :]
    col = grid[:, c]
    tree = grid[r, c]

    # Can see on row?
    lhs = row[:c]
    rhs = row[c + 1:]
    row_vis = np.all(lhs < tree) or np.all(rhs < tree)

    # Can see on col?
    top = col[:r]
    bot = col[r + 1:]
    col_vis = np.all(top < tree) or np.all(bot < tree)

    if row_vis or col_vis:
        count += 1


n_seen = count + 4*nrow - 4
print(f"A ::: {n_seen}")

def vis_score(value, vec):
    count = 0
    for v in vec:
        if v < value:
            count += 1
        elif v >= value:
            count += 1
            break
    return count

scores = []
for r, c in product(range(1, nrow - 1), range(1, ncol - 1)):
    west = grid[r, :c]
    east = grid[r, c + 1:]
    north = grid[:r, c]
    south = grid[r + 1:, c]
    value = grid[r, c]

    tree = grid[r, c]

    e_score = vis_score(value, east)
    s_score = vis_score(value, south)
    w_score = vis_score(value, west[::-1])
    n_score = vis_score(value, north[::-1])

    scenic_score = e_score*s_score*w_score*n_score
    scores.append((r, c, scenic_score))

r, c, best_score = max(scores, key=lambda t: t[2])

print(f"B ::: {best_score} at {(r, c)}")
