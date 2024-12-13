import re

import numpy as np


def main():
    claw_re = re.compile(
        r"A: X\+(\d+), Y\+(\d+).*?B: X\+(\d+), Y\+(\d+).*?X=(\d+), Y=(\d+)", re.DOTALL
    )

    with open("input.txt") as f:
        claw_machines = claw_re.findall(f.read())

    total = 0

    for claw_machine in claw_machines:
        ax, ay, bx, by, px, py = (int(_) for _ in claw_machine)

        px += 10_000_000_000_000
        py += 10_000_000_000_000

        left = np.array([[ax, bx], [ay, by]])
        right = np.array([px, py])

        a, b = (round(_) for _ in np.linalg.solve(left, right))
        if a * ax + b * bx == px and a * ay + b * by == py:
            total += a * 3 + b

    print(total)


if __name__ == "__main__":
    main()
