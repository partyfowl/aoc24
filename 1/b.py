import re

regex = re.compile(r"(\d+)\s+(\d+)")
matches = regex.findall(open("input.txt").read())

left = []
right = []

for l, r in matches:
    left.append(int(l))
    right.append(int(r))

total = 0

for l in left:
    total += l * right.count(l)

print(total)
