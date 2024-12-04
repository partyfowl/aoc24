import re

regex = re.compile(r"mul\((\d+),(\d+)\)")

matches = regex.findall(open("input.txt").read())

total = 0

for x, y in matches:
    total += int(x) * int(y)

print(total)
