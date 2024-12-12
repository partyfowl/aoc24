def get_border_lines(shape_original: set[complex]):
    borders = 0

    # Check north, south, east, west borders individually
    for i, j in ((1, 1j), (1, -1j), (-1, 1j), (-1, -1j)):
        shape_copy = shape_original.copy()
        while shape_copy:
            current = shape_copy.pop()
            if current + i not in shape_original:
                borders += 1
                for traverse_direction in (j, -j):
                    traverse = current
                    while (
                        traverse in shape_original
                        and traverse + i not in shape_original
                    ):
                        shape_copy.discard(traverse)
                        traverse += traverse_direction

    return borders


def fill_shape(grid: list[str], coord: complex, value: str, shape: set[complex]):
    for diff in (1, 1j, -1, -1j):
        test_coord = coord + diff
        y = int(test_coord.real)
        x = int(test_coord.imag)
        if y < 0 or x < 0:
            continue
        try:
            if test_coord in shape:
                # this coordinate has already been processed, move on
                continue
            if grid[y][x] == value:
                shape.add(test_coord)
                fill_shape(grid=grid, coord=test_coord, value=value, shape=shape)

        except IndexError:
            pass


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
        fill_shape(
            grid=grid,
            coord=start,
            value=grid[int(start.real)][int(start.imag)],
            shape=shape,
        )

        total += len(shape) * get_border_lines(shape)

        for coord in shape:
            coords.discard(coord)

        # break

    print(total)


if __name__ == "__main__":
    main()
