import re
import sys
from timeit import timeit

sys.setrecursionlimit(5000)  # 70 * 70 = 4900


def print_grid(grid_size, blocked):
    for y in range(-1, grid_size + 1):
        for x in range(-1, grid_size + 1):
            if complex(x, y) in blocked:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def solve_maze(
    blocked: set[complex], end: complex, position: complex, path: set[complex]
) -> list[complex]:

    if position == end:
        return [path]

    if position in blocked or position in path:
        return []

    path.add(position)

    viable_paths = []
    for direction in (1j, 1, -1j, -1):
        if viable_path := solve_maze(blocked, end, position + direction, path.copy()):
            viable_paths.extend(viable_path)

    return viable_paths


def main():
    regex = re.compile(r"(\d+),(\d+)")

    grid_size = 71
    filename = "input.txt"

    with open(filename) as f:
        coords = regex.findall(f.read())

    for bytes_fallen in range(len(coords), -1, -1):
        falling_bytes = (complex(int(coord[0]), int(coord[1])) for coord in coords)

        blocked = {next(falling_bytes) for _ in range(bytes_fallen)}

        # Add a border
        for i in range(grid_size):
            blocked.add(complex(-1, i))
            blocked.add(complex(i, -1))
            blocked.add(complex(grid_size, i))
            blocked.add(complex(i, grid_size))

        start = complex(0, 0)
        end = complex(grid_size - 1, grid_size - 1)

        paths = solve_maze(blocked, end, start, set())

        if paths == []:
            continue

        for coord in falling_bytes:
            valid_paths = []
            for path in paths:
                if coord not in path:
                    valid_paths.append(path)
            paths = valid_paths
            if paths == []:
                break
        break
    print(f"{int(coord.real)},{int(coord.imag)}")


if __name__ == "__main__":
    print(timeit(main, number=1))
