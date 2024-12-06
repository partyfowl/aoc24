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


def solve(grid: list[str]) -> int:
    # For a given grid, return 1 if a loop is found, 0 if not

    # Get initial position
    for y, row in enumerate(grid):
        if GUARD in row:
            position = (y, row.index(GUARD))
            break
    else:
        raise ValueError("Guard not found")
    # Initial direction is north - we are using y, x notation here
    direction = (-1, 0)

    directional_positions: set[tuple[tuple[int, int], tuple[int, int]]] = {
        (position, direction)
    }

    while True:
        # Matrix addition
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if grid[next_position[0]][next_position[1]] == OBSTACLE:
            direction = turn_right(direction)
            continue

        if grid[next_position[0]][next_position[1]] == BOUNDARY:
            break

        position = next_position
        directional_position = (position, direction)
        if directional_position in directional_positions:
            # If the guard is in a position and a direction he has been in before, he is in a loop
            return 1

        directional_positions.add(directional_position)

    return 0


def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    grid: list[list[str]] = []

    # Creating a border of ! around the grid. This will be our finish condition.
    for line in lines:
        grid.append([BOUNDARY, *line, BOUNDARY])

    grid.insert(0, [BOUNDARY] * len(grid[0]))
    grid.append([BOUNDARY] * len(grid[0]))

    grids = []

    # Brute force solution
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == GUARD:
                continue
            new_grid = [row.copy() for row in grid]
            new_grid[y][x] = OBSTACLE
            grids.append(new_grid)

    with Pool() as p:
        print(sum(p.map(solve, grids)))


if __name__ == "__main__":
    print(timeit.timeit(main, number=1))
    # 6.084375917009311 seconds
