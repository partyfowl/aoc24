import re
from collections import defaultdict
from math import prod

robot_re = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

width = 101
height = 103

total_spaces = width * height

quadrants = []

robots = []
with open("input.txt") as f:
    robots = [[int(_) for _ in _] for _ in robot_re.findall(f.read())]

counter = defaultdict(int)

seconds = 0

while True:
    show = False
    seconds += 1
    grid = set()

    for robot in robots:
        x, y, dx, dy = robot
        x = (x + dx) % width
        y = (y + dy) % height
        grid.add((x, y))
        robot[0] = x
        robot[1] = y

    for x, y in grid:
        for dy in range(1, 6):
            if (x, y + dy) not in grid:
                break
        else:  # nobreak
            show = True

    if show:
        for _ in range(100):
            print()
        for y in range(height):
            for x in range(width):
                print("#" if (x, y) in grid else " ", end="")
            print()

        # keep pressing enter until the tree appears
        input(seconds)
