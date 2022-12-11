import re
from collections import deque

raw = open('input.txt', 'r').readlines()

data = raw[:8]
indexer = raw[8]
instructs = raw[10:]

stacks = {}
for col in range(1, 10):
    ix = indexer.find(str(col))
    stacks[col] = deque([row[ix] for row in data if row[ix] != ' '])

for instruct in instructs:
    res = re.findall('move (\d+) from (\d) to (\d)', instruct)[0]
    how_many, from_, to_ = [int(i) for i in res]

    for _ in range(how_many):
        stacks[to_].appendleft(stacks[from_].popleft())

tops = ''.join(stacks[i][0] for i in range(1, 10))

print(f"A ::: {tops}")

stacks = {}
for col in range(1, 10):
    ix = indexer.find(str(col))
    stacks[col] = [row[ix] for row in data if row[ix] != ' ']

for instruct in instructs:
    res = re.findall('move (\d+) from (\d) to (\d)', instruct)[0]
    how_many, from_, to_ = [int(i) for i in res]

    moved_crates = stacks[from_][:how_many]
    stacks[from_] = stacks[from_][how_many:]
    stacks[to_] = moved_crates + stacks[to_]

tops = ''.join(stacks[i][0] for i in range(1, 10))

print(f"B ::: {tops}")
