import re
from collections import defaultdict
from itertools import combinations

complicated_regex = re.compile(r"\w")

antennas: defaultdict[str, set[complex]] = defaultdict(set)
antinodes: set[complex] = set()

with open("input.txt") as f:
    for y, line in enumerate(f):
        for match in complicated_regex.finditer(line):
            # Abusing complex types for coordinates here
            antennas[match.group()].add(complex(y, match.start()))

max_y = y
max_x = len(line.strip()) - 1

for frequency in antennas.values():
    for a, b in combinations(frequency, r=2):
        # Thanks to the abuse of complex types, this matrix diff is nice and easy
        diff = a - b

        antinode = a
        while 0 <= int(antinode.real) <= max_y and 0 <= int(antinode.imag) <= max_x:
            antinodes.add(antinode)
            antinode = antinode + diff

        antinode = b
        while 0 <= int(antinode.real) <= max_y and 0 <= int(antinode.imag) <= max_x:
            antinodes.add(antinode)
            antinode = antinode - diff

print(len(antinodes))
