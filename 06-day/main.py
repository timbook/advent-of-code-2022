data = open('input.txt', 'r').read().strip()

def is_marker(s):
    return len(set(s)) == 4

def is_msg(s):
    return len(set(s)) == 14

for i in range(len(data) - 3):
    sub = data[i:i + 4]
    if is_marker(sub):
        break

print(i + 4)

for i in range(len(data) - 13):
    sub = data[i:i + 14]
    if is_msg(sub):
        break

print(i + 14)
