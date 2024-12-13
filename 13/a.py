import re


def main():
    claw_re = re.compile(
        r"A: X\+(\d+), Y\+(\d+).*?B: X\+(\d+), Y\+(\d+).*?X=(\d+), Y=(\d+)", re.DOTALL
    )

    with open("input.txt") as f:
        claw_machines = claw_re.findall(f.read())

    total = 0

    for claw_machine in claw_machines:
        ax, ay, bx, by, px, py = (int(_) for _ in claw_machine)

        b_press_count = 0

        # Work backwards, to understand how many times we would have to press the B button to
        # get to a point where the distance to the prize is divisible by the A button

        # This gives the correct answer for the input given, however it may not work for all inputs

        div_x, mod_x = divmod(px, ax)
        div_y, mod_y = divmod(py, ay)

        while (positive := div_x >= 0 and div_y >= 0) and not (
            div_x == div_y and mod_x == 0 and mod_y == 0
        ):
            px -= bx
            py -= by
            b_press_count += 1

            div_x, mod_x = divmod(px, ax)
            div_y, mod_y = divmod(py, ay)

        if positive:
            total += b_press_count + div_x * 3
    print(total)


if __name__ == "__main__":
    main()
