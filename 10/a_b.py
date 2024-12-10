from typing import Literal

BOUNDARY = "!"


def check_directions(
    grid: list[list[int | Literal["!"]]], location: complex, value: int = 0
) -> tuple[set[complex], int]:
    peaks = set()
    routes_count = 0
    for direction in (1, 1j, -1, -1j):
        lookahead = location + direction
        lookahead_value = grid[int(lookahead.real)][int(lookahead.imag)]
        if lookahead_value == BOUNDARY:
            continue
        elif lookahead_value == value + 1:
            if lookahead_value == 9:
                peaks.add(lookahead)
                routes_count += 1
            else:
                next_peaks, next_routes_count = check_directions(
                    grid, lookahead, lookahead_value
                )
                peaks.update(next_peaks)
                routes_count += next_routes_count
    return peaks, routes_count


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

    total_1 = 0
    total_2 = 0

    for trailhead in trailheads:
        unique_peaks, routes = check_directions(grid, trailhead)
        total_1 += len(unique_peaks)
        total_2 += routes

    print("Part 1:", total_1)
    print("Part 2:", total_2)


if __name__ == "__main__":
    main()
