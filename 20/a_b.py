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


def main(part: int):
    with open("input.txt") as f:
        grid = [_.strip() for _ in f.readlines()]

    end = next(
        complex(y, line.index("E")) for y, line in enumerate(grid) if "E" in line
    )
    start = next(
        complex(y, line.index("S")) for y, line in enumerate(grid) if "S" in line
    )

    vanilla_path = run_race(grid, start, end)  # 85 - off by one but this is fine

    if part == 1:
        cheat_duration = 2
    elif part == 2:
        cheat_duration = 20

    possible_cheats = {
        sum(_)
        for _ in combinations_with_replacement((1, -1, 0, 1j, -1j), r=cheat_duration)
    }

    total = 0

    path_forwards = set(vanilla_path)
    location_index = {k: v for v, k in enumerate(vanilla_path)}

    for i, location in enumerate(vanilla_path):
        path_forwards.remove(location)

        for cheat in possible_cheats:
            cheat_location = location + cheat
            if cheat_location in path_forwards:

                time_saved = (
                    location_index[cheat_location] - i
                ) - get_cheat_distance_travelled(cheat)

                if time_saved >= 100:
                    total += 1

    print(f"Part {part}: {total}")


if __name__ == "__main__":
    print(timeit(lambda: main(1), number=1))
    # 0.5023840590001782 seconds
    print(timeit(lambda: main(2), number=1))
    # 1.6199745970006916 seconds
