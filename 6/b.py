import timeit
from multiprocessing.pool import Pool

BOUNDARY = "!"
OBSTACLE = "#"
GUARD = "^"


def turn_right(direction: tuple[int, int]) -> tuple[int, int]:
    # Probably a more elegant maths-y way to do this
    y, x = direction
    if y == -1:
        return (0, 1)
    elif x == 1:
        return (1, 0)
    elif y == 1:
        return (0, -1)
    elif x == -1:
        return (-1, 0)


def get_start_position(grid: list[list[str]]) -> tuple[int, int]:
    # Get initial position
    for y, row in enumerate(grid):
        if GUARD in row:
            return (y, row.index(GUARD))
    else:  # nobreak
        raise ValueError("Guard not found")


def get_path_positions(
    grid: list[list[str]], position: tuple[int, int]
) -> set[tuple[int, int]]:
    # Initial direction is north - we are using y, x notation here
    direction = (-1, 0)

    # Include the initial position here. We use a set so we can keep track of unique positions
    positions: set[tuple[int, int]] = {position}

    while True:
        # Matrix addition
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if grid[next_position[0]][next_position[1]] == OBSTACLE:
            direction = turn_right(direction)
            continue

        if grid[next_position[0]][next_position[1]] == BOUNDARY:
            break

        position = next_position
        positions.add(position)

    return positions


def solve(grid: list[list[str]], position: tuple[int, int]) -> int:
    # For a given grid, return 1 if a loop is found, 0 if not

    # Initial direction is north - we are using y, x notation here
    direction = (-1, 0)

    directional_positions: set[tuple[tuple[int, int], tuple[int, int]]] = {
        (position, direction)
    }

    while True:
        # Extra loop here to only store directional positions on change of direction
        while True:
            # Matrix addition
            lookahead = (position[0] + direction[0], position[1] + direction[1])

            if grid[lookahead[0]][lookahead[1]] == OBSTACLE:
                direction = turn_right(direction)
                break

            if grid[lookahead[0]][lookahead[1]] == BOUNDARY:
                return 0

            position = lookahead

        directional_position = (position, direction)
        if directional_position in directional_positions:
            # If the guard is in a position and a direction he has been in before, he is in a loop
            return 1

        directional_positions.add(directional_position)


def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    grid: list[list[str]] = []

    # Creating a border of ! around the grid. This will be our finish condition.
    for line in lines:
        grid.append([BOUNDARY, *line, BOUNDARY])

    grid.insert(0, [BOUNDARY] * len(grid[0]))
    grid.append([BOUNDARY] * len(grid[0]))

    args_list = []

    # Only get the start position once
    start_position = get_start_position(grid)

    # Only checking positions on the original path
    path_positions = get_path_positions(grid, start_position)

    # Brute force solution
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == GUARD or (y, x) not in path_positions:
                continue
            new_grid = [row.copy() for row in grid]
            new_grid[y][x] = OBSTACLE
            args_list.append((new_grid, start_position))

    with Pool() as p:
        print(sum(p.starmap(solve, args_list)))


if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
    # 1.1242980000000102 seconds
