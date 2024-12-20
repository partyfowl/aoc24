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


def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")

    grid: list[str] = []

    # Creating a border of ! around the grid. This will be our finish condition.
    for line in lines:
        grid.append(f"{BOUNDARY}{line}{BOUNDARY}")

    grid.insert(0, BOUNDARY * len(grid[0]))
    grid.append(BOUNDARY * len(grid[0]))

    # Get initial position
    for y, row in enumerate(grid):
        if GUARD in row:
            position = (y, row.index(GUARD))
            break

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

    print(len(positions))


if __name__ == "__main__":
    main()
