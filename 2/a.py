reports = open("input.txt").read().split("\n")

total_safe = 0

for report in reports:
    levels = [int(_) for _ in report.split(" ")]

    direction = ""
    safe = True

    for previous_index, level in enumerate(levels[1:]):
        diff = level - levels[previous_index]
        if diff == 0 or abs(diff) > 3:
            safe = False
            break
        if diff > 0:
            if direction == "":
                direction = "+"
            elif direction == "-":
                safe = False
                break
        else:
            if direction == "":
                direction = "-"
            elif direction == "+":
                safe = False
                break

    if safe:
        total_safe += 1

print(total_safe)
