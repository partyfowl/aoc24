from collections import defaultdict
from functools import cache
from timeit import timeit
from typing import Literal

BOUNDARY = "!"


@cache  # Cache known paths to peaks, reduces runtime by ~50%
def check_directions(
    grid: tuple[tuple[int | Literal["!"]]], location: complex, value: int = 0
) -> defaultdict[str, int]:
    peaks: defaultdict[str, int] = defaultdict(int)
    for direction in (1, 1j, -1, -1j):
        lookahead = location + direction
        lookahead_value = grid[int(lookahead.real)][int(lookahead.imag)]
        if lookahead_value == BOUNDARY:
            continue
        elif lookahead_value == value + 1:
            if lookahead_value == 9:
                peaks[lookahead] += 1
            else:
                for k, v in check_directions(grid, lookahead, lookahead_value).items():
                    peaks[k] += v
    return peaks


def main():
    trailheads: set[complex] = set()

    with open("input.txt") as f:
        grid: list[list[int | Literal["!"]]] = []
        for y, line in enumerate(f):
            grid.append([BOUNDARY])
            for x, char in enumerate(line.strip()):
                if char == "0":
                    trailheads.add(
                        complex(y + 1, x + 1)
                    )  # + 1 here to account for boundaries
                grid[-1].append(int(char))
            grid[-1].append(BOUNDARY)
        grid.insert(0, [BOUNDARY] * len(grid[0]))
        grid.append(grid[0])

    # Make this a tuple so it's hashable, so we can cache responses for known paths
    grid_tuple: tuple[tuple[int | Literal["!"]]] = tuple(tuple(_) for _ in grid)

    total_1 = 0
    total_2 = 0

    for trailhead in trailheads:
        peaks = check_directions(grid_tuple, trailhead)
        total_1 += len(peaks)
        total_2 += sum(peaks.values())

    print("Part 1:", total_1)
    print("Part 2:", total_2)


if __name__ == "__main__":
    print(timeit(main, number=100))
