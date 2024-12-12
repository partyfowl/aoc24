def fill_shape(grid: list[str], coord: complex, value: str, shape: set[complex]) -> int:
    # Fill the shape set with coordinates, and also return the borders
    borders = 0

    for diff in (1, 1j, -1, -1j):
        test_coord = coord + diff
        y = int(test_coord.real)
        x = int(test_coord.imag)
        if y < 0 or x < 0:
            borders += 1
            continue
        try:
            if test_coord in shape:
                # this coordinate has already been processed, move on
                continue
            if grid[y][x] == value:
                shape.add(test_coord)
                borders += fill_shape(
                    grid=grid, coord=test_coord, value=value, shape=shape
                )
            else:
                borders += 1

        except IndexError:
            borders += 1

    return borders


def main():
    coords: set[complex] = set()
    grid: list[str] = []
    y = 0
    x = 0
    row = ""
    with open("input.txt") as f:
        while char := f.read(1):
            if char == "\n":
                grid.append(row)
                row = ""
                x = 0
                y += 1
                continue
            row += char
            coords.add(complex(y, x))
            x += 1

        grid.append(row)

    total = 0

    while coords:
        start = coords.pop()
        shape = set((start,))
        borders = fill_shape(
            grid=grid,
            coord=start,
            value=grid[int(start.real)][int(start.imag)],
            shape=shape,
        )
        total += len(shape) * borders

        for coord in shape:
            coords.discard(coord)

    print(total)


if __name__ == "__main__":
    main()
