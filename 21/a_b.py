from functools import cache
from itertools import product
from timeit import timeit

DOOR_KEYPAD = {
    "7": 0 + 0j,
    "8": 0 + 1j,
    "9": 0 + 2j,
    "4": 1 + 0j,
    "5": 1 + 1j,
    "6": 1 + 2j,
    "1": 2 + 0j,
    "2": 2 + 1j,
    "3": 2 + 2j,
    # nothing at 3 + 0 j
    None: 3 + 0j,
    "0": 3 + 1j,
    "A": 3 + 2j,
}

ROBOT_KEYPAD = {
    # nothing at 0 + 0 j
    None: 0 + 0j,
    "^": 0 + 1j,  # ^
    "A": 0 + 2j,
    "<": 1 + 0j,  # <
    "v": 1 + 1j,  # v
    ">": 1 + 2j,  # >
}

DIRECTIONS = {"^": -1, ">": 1j, "v": 1, "<": -1j}


@cache
def find_paths(position: complex, destination: complex, avoid: complex):
    movement = destination - position

    movements = ""

    y = abs(int(movement.real))
    if movement.real > 0:
        movements += "v" * y
    else:
        movements += "^" * y

    x = abs(int(movement.imag))
    if movement.imag > 0:
        movements += ">" * x
    else:
        movements += "<" * x

    paths = (movements, movements[::-1])

    start_position = position
    viable_paths = set()

    for path in paths:
        position = start_position
        for direction in path:
            position += DIRECTIONS[direction]
            if position == avoid:
                break
        else:  # nobreak
            viable_paths.add(path + "A")

    return viable_paths


@cache
def robot_recurse(code: str, robot_keypad: bool, remaining_robots: int) -> int:
    if robot_keypad:
        keypad = ROBOT_KEYPAD
    else:
        keypad = DOOR_KEYPAD
    if remaining_robots == 0:
        return len(code)

    position = keypad["A"]

    paths = []

    for digit in code:
        paths.append(find_paths(position, keypad[digit], keypad[None]))
        position = keypad[digit]

    # We can process each direction 1 by 1 here, as the robots must reset back to A
    # at the end of each move .This allows us to cache the end result/requirement for
    # each character, making this much faster
    return min(
        sum(robot_recurse(code, True, remaining_robots - 1) for code in options)
        for options in product(*paths)
    )


def solve(codes: list[str], total_robots) -> int:
    total = 0
    for code in codes:
        total += robot_recurse(code, False, total_robots) * int(code.strip("A"))
    return total


def main():
    with open("input.txt") as f:
        codes = f.read().splitlines()

    print("Part 1:", solve(codes, 3))
    print("Part 2:", solve(codes, 26))


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 0.0020929999991494697
