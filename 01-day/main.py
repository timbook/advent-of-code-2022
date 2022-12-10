raw = open('input.txt', 'r').readlines()

data = []
total = 0

for item in raw:
    if item.strip() == '':
        data.append(total)
        total = 0
    else:
        total += int(item.strip())

print(f"A ::: {max(data)}")

print(f"B ::: {sum(sorted(data)[-3:])}")
