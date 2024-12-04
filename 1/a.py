import re

regex = re.compile(r"(\d+)\s+(\d+)")
matches = regex.findall(open("input.txt").read())

left = []
right = []

for l, r in matches:
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

total = 0

for i in range(len(matches)):
    total += abs(left[i] - right[i])

print(total)
