import re
from collections import deque


def swap(instructions: deque[tuple[str, str, str, str]], index1, index2):
    a = instructions[index1]
    b = instructions[index2]
    instructions[index1] = a[:3] + b[3:]
    instructions[index2] = b[:3] + a[3:]


def main():
    gates_re = re.compile(r"(\w{3}) (\w+) (\w{3}) -> (\w{3})")

    states: dict[str, int] = {}
    instructions: deque[tuple[str, str, str, str]] = deque()

    with open("input.txt") as f:
        while line := f.readline():
            if match := gates_re.match(line):
                instructions.append(match.groups())

    bad = set()

    for a, operator, b, target in instructions:
        if target.startswith("z") and target != "z45":
            if operator != "XOR":
                print(a, operator, b, target)
                bad.add(target)
                # z19, z33, z13
        elif not (
            a.startswith("x")
            or a.startswith("y")
            or b.startswith("x")
            or b.startswith("y")
        ):
            if operator == "XOR":
                print(a, operator, b, target)
                bad.add(target)
        if (
            a.startswith("x")
            or a.startswith("y")
            or b.startswith("x")
            or b.startswith("y")
        ):
            if "00" in a:
                continue
            if operator == "XOR":
                for _ in instructions:
                    if (_[0] == target or _[2] == target) and _[1] == "XOR":
                        break
                else:  # nobreak
                    bad.add(target)
            if operator == "AND":
                for _ in instructions:
                    if (_[0] == target or _[2] == target) and _[1] == "OR":
                        break
                else:  # nobreak
                    bad.add(target)
    print(",".join(sorted(bad)))


if __name__ == "__main__":
    main()
