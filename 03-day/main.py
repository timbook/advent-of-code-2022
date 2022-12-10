from string import ascii_letters

lines = open('input.txt', 'r').readlines()
lines = [line.strip() for line in lines]

letter_score = lambda x: ascii_letters.find(x) + 1

priorities = []

for line in lines:
    h = len(line) // 2
    lhs = set(line[:h])
    rhs = set(line[h:])

    item = list(lhs & rhs)[0]

    priorities.append(letter_score(item))

print(f"A ::: {sum(priorities)}")

priorities = []
n_groups = len(lines) // 3
for i in range(n_groups):
    bag1 = set(lines[3*i])
    bag2 = set(lines[3*i + 1])
    bag3 = set(lines[3*i + 2])

    item = list(bag1 & bag2 & bag3)[0]
    priorities.append(letter_score(item))

print(f"B ::: {sum(priorities)}")
