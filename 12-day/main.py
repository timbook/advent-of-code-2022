import networkx as nx
import numpy as np
from itertools import product

hmap = open('input.txt').readlines()

grid = np.array([list(line) for line in hmap])

srow, scol = np.where(grid == 'S')
start_node = (srow[0], scol[0])

erow, ecol = np.where(grid == 'E')
end_node = (erow[0], ecol[0])

a_locs = np.where((grid == 'a') | (grid == 'S'))

@np.vectorize
def np_to_ord(x):
    if x == 'S':
        return ord('a')
    elif x == 'E':
        return ord('z')
    else:
        return ord(x)

grid = np_to_ord(grid)

nrow, ncol = grid.shape

G = nx.DiGraph()

# Create nodes
for r, c in product(range(nrow), range(ncol)):
    G.add_node((r, c))
    
# Create edges
for r, c in product(range(nrow), range(ncol)):
    val = grid[r, c]

    nb_locs = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
    nb_locs = [(r, c) for r, c in nb_locs if r >= 0 and c >= 0]
    for nb_loc in nb_locs:
        try:
            nb = grid[nb_loc[0], nb_loc[1]]
            if nb - val <= 1:
                G.add_edge((r, c), nb_loc)
        except:
            pass

res = nx.dijkstra_path(G, start_node, end_node)
sol_a = len(res) - 1
print(f"A ::: {sol_a}")

path_lens = []
for start_r, start_c in zip(*a_locs):
    try:
        path = nx.dijkstra_path(G, (start_r, start_c), end_node)
        path_lens.append(len(path) - 1)
    except:
        pass

sol_b = min(path_lens)
print(f"B ::: {sol_b}")
