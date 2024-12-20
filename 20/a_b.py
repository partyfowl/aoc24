from functools import cache
from itertools import combinations_with_replacement
from timeit import timeit


@cache
def get_cheat_distance_travelled(cheat: complex) -> int:
    return int(abs(cheat.real) + abs(cheat.imag))


def run_race(
    grid: list[str],
    start: complex,
    end: complex,
) -> dict[complex, int]:
    index = 0

    # As of Python 3.7, regular dicts are guaranteed to be ordered.
    path_taken: dict[complex, int] = {start: index}
    position = start

    directions = (-1, 1j, 1, -1j)

    while position != end:
        for direction in directions:
            next_position = position + direction
            if next_position in path_taken:
                continue
            while grid[int(next_position.real)][int(next_position.imag)] != "#":
                index += 1
                position = next_position
                path_taken[position] = index
                next_position += direction

    return path_taken


def solve(
    max_cheat_duration: int, path: dict[complex, int], path_forwards: set[complex]
):
    possible_cheats = tuple(
        {
            sum(_)
            for _ in combinations_with_replacement(
                (1, -1, 0, 1j, -1j), r=max_cheat_duration
            )
        }
    )

    total = 0

    for location, i in path.items():
        path_forwards.discard(location)

        for cheat in possible_cheats:
            cheat_location = location + cheat
            if cheat_location in path_forwards:

                time_saved = (path[cheat_location] - i) - get_cheat_distance_travelled(
                    cheat
                )

                if time_saved >= 100:
                    total += 1

    return total


def main():
    with open("input.txt") as f:
        grid = []
        line = ""
        y = 0
        x = 0
        while char := f.read(1):
            if char == "\n":
                grid.append(line)
                line = ""
                y += 1
                x = 0
            else:
                line += char
                if char == "E":
                    end = complex(y, x)
                elif char == "S":
                    start = complex(y, x)
                x += 1
        grid.append(line)

    path = run_race(grid, start, end)  # 85 - off by one but this is fine

    # Sets are faster than lists for lookups
    path_forwards = set(path)

    print("Part 1:", solve(2, path, path_forwards.copy()))
    print("Part 2:", solve(20, path, path_forwards))


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 1.1088037389999954 seconds
