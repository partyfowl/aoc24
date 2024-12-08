import re
from collections import defaultdict
from itertools import combinations


complicated_regex = re.compile(r"\w")

antennas: defaultdict[str, set[tuple[int, int]]] = defaultdict(set)
antinodes: set[tuple[int, int]] = set()

with open("input.txt") as f:
    for y, line in enumerate(f):
        for match in complicated_regex.finditer(line):
            antenna = (y, match.start())
            antennas[match.group()].add(antenna)
            antinodes.add(antenna)

max_y = y
max_x = len(line) - 1

for frequency in antennas.values():
    for a, b in combinations(frequency, r=2):
        diff_y = b[0] - a[0]
        diff_x = b[1] - a[1]

        antinode = (b[0] + diff_y, b[1] + diff_x)
        while (
            antinode[0] >= 0
            and antinode[1] >= 0
            and antinode[0] <= max_y
            and antinode[1] <= max_x
        ):
            antinodes.add(antinode)
            antinode = (antinode[0] + diff_y, antinode[1] + diff_x)

        antinode = (a[0] - diff_y, a[1] - diff_x)
        while (
            antinode[0] >= 0
            and antinode[1] >= 0
            and antinode[0] <= max_y
            and antinode[1] <= max_x
        ):
            antinodes.add(antinode)
            antinode = (antinode[0] - diff_y, antinode[1] - diff_x)

print(len(antinodes))
