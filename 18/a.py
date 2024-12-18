import re
import sys
from timeit import timeit

sys.setrecursionlimit(5000)  # 70 * 70 = 4900

lowest_score_seen = {}


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
) -> int | None:

    if position == end:
        return len(path)

    if position in blocked or position in path:
        return

    if position in lowest_score_seen and len(path) >= lowest_score_seen[position]:
        return

    lowest_score_seen[position] = len(path)

    path.add(position)

    scores = {
        solve_maze(blocked, end, position + direction, path.copy())
        for direction in (1j, 1, -1j, -1)
    }
    scores.discard(None)

    if scores:
        return min(scores)


def main():
    regex = re.compile(r"(\d+),(\d+)")
    bytes_fallen = 1024
    grid_size = 71
    filename = "input.txt"

    # bytes_fallen = 12
    # grid_size = 7
    # filename = "test.txt"

    with open(filename) as f:
        blocked = {
            complex(int(coord[0]), int(coord[1]))
            for coord in regex.findall(f.read())[:bytes_fallen]
        }

    print(blocked)
    # Add a border
    for i in range(grid_size):
        blocked.add(complex(-1, i))
        blocked.add(complex(i, -1))
        blocked.add(complex(grid_size, i))
        blocked.add(complex(i, grid_size))

    start = complex(0, 0)
    end = complex(grid_size - 1, grid_size - 1)

    print_grid(grid_size, blocked)

    score = solve_maze(blocked, end, start, set())

    print(score)


if __name__ == "__main__":
    print(timeit(main, number=1))
