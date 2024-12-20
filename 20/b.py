from itertools import combinations_with_replacement
from timeit import timeit


def run_race(
    grid: list[str],
    start: complex,
    end: complex,
):
    path_taken: list[complex] = [start]
    position = start

    while position != end:
        for direction in (-1, 1j, 1, -1j):
            next_position = position + direction
            if next_position in path_taken:
                continue
            if grid[int(next_position.real)][int(next_position.imag)] != "#":
                break

        while grid[int(next_position.real)][int(next_position.imag)] != "#":
            position = next_position
            path_taken.append(position)
            next_position += direction

    return path_taken


def main():
    with open("input.txt") as f:
        grid = [_.strip() for _ in f.readlines()]

    end = next(
        complex(y, line.index("E")) for y, line in enumerate(grid) if "E" in line
    )
    start = next(
        complex(y, line.index("S")) for y, line in enumerate(grid) if "S" in line
    )

    vanilla_path = run_race(grid, start, end)  # 85 - off by one but this is fine

    cheat_duration = 20
    possible_cheats = {
        sum(_)
        for _ in combinations_with_replacement((1, -1, 0, 1j, -1j), r=cheat_duration)
    }

    total = 0

    for i, location in enumerate(vanilla_path):
        path_forwards = vanilla_path[i + 1 :]

        for cheat in possible_cheats:
            cheat_location = location + cheat
            if cheat_location in path_forwards:

                time_saved = (vanilla_path.index(cheat_location) - i) - int(
                    abs(cheat.real) + abs(cheat.imag)
                )

                if time_saved >= 100:
                    total += 1

    print(total)


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 521.8434703479979 seconds
