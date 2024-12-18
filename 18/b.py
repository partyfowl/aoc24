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
    blocked: list[complex], end: complex, position: complex, path: set[complex]
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

    # Keep blocked as a set of coordinates - this is faster than using the order list directly
    blocked: set[complex] = set()

    # Keep a list of the coordinates in order, we will pop these later
    order: list[complex] = []

    with open(filename) as f:
        for match in regex.findall(f.read()):
            this = complex(int(match[0]), int(match[1]))
            blocked.add(this)
            order.append(this)

    # Add a border - not necessary, but makes out of bounds checking easy
    for i in range(grid_size):
        blocked.add(complex(-1, i))
        blocked.add(complex(i, -1))
        blocked.add(complex(grid_size, i))
        blocked.add(complex(i, grid_size))

    start = complex(0, 0)
    end = complex(grid_size - 1, grid_size - 1)

    # We work backwards, starting with all bytes blocked, removing them 1 by 1 until a path is available
    while not solve_maze(blocked, end, start, set()):
        answer = order.pop()
        blocked.discard(answer)

    print(f"{int(answer.real)},{int(answer.imag)}")


if __name__ == "__main__":
    print(timeit(main, number=1))
