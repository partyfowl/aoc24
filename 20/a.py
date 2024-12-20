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

    possible_cheats = []

    for y, line in enumerate(grid[1:-1], 1):
        for x, char in enumerate(line[1:-1], 1):
            if char == "#":
                if (
                    sum(
                        (
                            grid[y + 1][x] != "#",
                            grid[y - 1][x] != "#",
                            grid[y][x + 1] != "#",
                            grid[y][x - 1] != "#",
                        )
                    )
                    >= 2
                ):
                    possible_cheats.append(complex(y, x))

    total = 0

    for cheat in possible_cheats:
        adjacent_points = []
        for i, location in enumerate(vanilla_path):
            for direction in (-1, 1j, 1, -1j):
                if location + direction == cheat:
                    adjacent_points.append(i)
                    break

        time_saved = (adjacent_points[-1] - adjacent_points[0]) - 2
        if time_saved >= 100:
            total += 1

    print(total)


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 23.204495396999846 seconds
