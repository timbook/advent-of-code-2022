import re
import numpy as np

lines = open('input.txt', 'r').readlines()

count = 0
for line in lines:
    nums = re.findall('(\d+)-(\d+),(\d+)-(\d+)', line.strip())[0]
    a, b, c, d = [int(i) for i in nums]
    
    cond1 = (a <= c) and (d <= b)
    cond2 = (c <= a) and (b <= d)

    if cond1 or cond2:
        count += 1
    
print(f"A ::: {count}")

count = 0
for line in lines:
    nums = re.findall('(\d+)-(\d+),(\d+)-(\d+)', line.strip())[0]
    a, b, c, d = [int(i) for i in nums]

    arr1 = np.arange(a, b + 1)
    arr2 = np.arange(c, d + 1)

    if len(np.intersect1d(arr1, arr2)) > 0:
        count += 1

print(f"B ::: {count}")
