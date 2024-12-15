class Warehouse:
    def __init__(
        self,
        boundaries: set[tuple[int, int]],
        boxes: set[tuple[int, int]],
        robot: set[tuple[int, int]],
    ):
        self.boundaries = boundaries
        self.boxes = boxes
        self.robot = robot

    def _check_next_loc(
        self,
        grid_ref: tuple[int, int],
        direction: tuple[int, int],
    ):

        next_grid_ref = (grid_ref[0] + direction[0], grid_ref[1] + direction[1])

        if next_grid_ref in self.boundaries:
            return False

        if next_grid_ref in self.boxes:
            return self._check_next_loc(next_grid_ref, direction)

        return True

    def _move(
        self,
        grid_ref: tuple[int, int],
        direction: tuple[int, int],
        this_set: set[tuple[int, int]],
    ):
        if not self._check_next_loc(
            grid_ref=grid_ref,
            direction=direction,
        ):
            return

        next_grid_ref = (grid_ref[0] + direction[0], grid_ref[1] + direction[1])

        if next_grid_ref in self.boxes:
            self._move(next_grid_ref, direction, self.boxes)

        this_set.remove(grid_ref)
        this_set.add(next_grid_ref)

    def move_robot(self, direction):
        self._move(*self.robot, direction, self.robot)

    def total(self) -> int:
        total = 0
        for y, x in self.boxes:
            total += y * 100 + x
        return total


def main():
    directional_vectors = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

    y = 0
    x = 0
    boundaries = set()
    boxes = set()
    robot = set()
    directions = []

    with open("input.txt") as f:
        while (char := f.read(1)) and not (char == "\n" and x == 0):
            if char == "\n":
                y += 1
                x = 0
            else:
                if char == ".":
                    pass
                elif char == "#":
                    boundaries.add((y, x))
                elif char == "O":
                    boxes.add((y, x))
                elif char == "@":
                    robot.add((y, x))
                x += 1

        while char := f.read(1):
            if direction := directional_vectors.get(char):
                directions.append(direction)

    warehouse = Warehouse(boundaries=boundaries, boxes=boxes, robot=robot)

    for direction in directions:
        warehouse.move_robot(direction)

    print(warehouse.total())


if __name__ == "__main__":
    main()
