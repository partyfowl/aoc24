import re
from collections import defaultdict
from math import prod

robot_re = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

width = 101
height = 103

quadrants = []

for i in ((0, width // 2), (width - width // 2, width)):
    for j in ((0, height // 2), (height - height // 2, height)):
        quadrants.append((i, j))

print(quadrants)

robots = []
with open("input.txt") as f:
    robots = [[int(_) for _ in _] for _ in robot_re.findall(f.read())]

quadrants_counter = defaultdict(int)

for x, y, dx, dy in robots:
    x = (x + dx * 100) % width
    y = (y + dy * 100) % height

    for quadrant in quadrants:
        (x_min, x_max), (y_min, y_max) = quadrant
        if x_min <= x < x_max and y_min <= y < y_max:
            quadrants_counter[quadrant] += 1

print(prod(quadrants_counter.values()))
