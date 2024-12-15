class Warehouse:
    def __init__(
        self,
        boundaries: set[tuple[int, int]],
        boxes_l: set[tuple[int, int]],
        boxes_r: set[tuple[int, int]],
        robot: set[tuple[int, int]],
    ):
        self.boundaries = boundaries
        self.boxes_l = boxes_l
        self.boxes_r = boxes_r
        self.robot = robot

    def _check_next_loc(
        self,
        grid_ref: tuple[int, int],
        direction: tuple[int, int],
    ):

        next_grid_ref = (grid_ref[0] + direction[0], grid_ref[1] + direction[1])

        if next_grid_ref in self.boundaries:
            return False

        if direction[0]:  # up/down
            if next_grid_ref in self.boxes_l:
                return self._check_next_loc(
                    next_grid_ref, direction
                ) and self._check_next_loc(
                    (next_grid_ref[0], next_grid_ref[1] + 1), direction
                )

            if next_grid_ref in self.boxes_r:
                return self._check_next_loc(
                    next_grid_ref, direction
                ) and self._check_next_loc(
                    (next_grid_ref[0], next_grid_ref[1] - 1), direction
                )
        else:  # left/right
            if next_grid_ref in self.boxes_l:
                return self._check_next_loc(next_grid_ref, direction)
            if next_grid_ref in self.boxes_r:
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

        if direction[0]:  # up/down
            if next_grid_ref in self.boxes_l:
                self._move(next_grid_ref, direction, self.boxes_l)
                self._move(
                    (next_grid_ref[0], next_grid_ref[1] + 1), direction, self.boxes_r
                )

            elif next_grid_ref in self.boxes_r:
                self._move(next_grid_ref, direction, self.boxes_r)
                self._move(
                    (next_grid_ref[0], next_grid_ref[1] - 1), direction, self.boxes_l
                )

        else:  # left/right
            if next_grid_ref in self.boxes_l:
                self._move(next_grid_ref, direction, self.boxes_l)

            elif next_grid_ref in self.boxes_r:
                self._move(next_grid_ref, direction, self.boxes_r)

        this_set.remove(grid_ref)
        this_set.add(next_grid_ref)

    def move_robot(self, direction):
        self._move(*self.robot, direction, self.robot)

    def total(self) -> int:
        total = 0
        for y, x in self.boxes_l:
            total += y * 100 + x
        return total


def main():
    directional_vectors = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

    y = 0
    x = 0
    boundaries = set()
    boxes_l = set()
    boxes_r = set()
    robot = set()
    directions = []

    with open("input.txt") as f:
        while (char := f.read(1)) and not (char == "\n" and x == 0):
            if char == "\n":
                y += 1
                x = 0
            else:
                for left in (True, False):
                    if char == ".":
                        pass
                    elif char == "#":
                        boundaries.add((y, x))
                    elif char == "O":
                        if left:
                            boxes_l.add((y, x))
                        else:
                            boxes_r.add((y, x))
                    elif char == "@" and left:
                        robot.add((y, x))
                    x += 1

        while char := f.read(1):
            if direction := directional_vectors.get(char):
                directions.append(direction)

    warehouse = Warehouse(
        boundaries=boundaries, boxes_l=boxes_l, boxes_r=boxes_r, robot=robot
    )

    for direction in directions:
        warehouse.move_robot(direction)

    print(warehouse.total())


if __name__ == "__main__":
    main()
