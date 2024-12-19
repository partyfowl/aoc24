from functools import cache
from timeit import timeit


@cache
def is_combination_viable(combo: str, towels: tuple[str, ...]):
    if combo == "":
        return 1

    total = 0

    for towel in towels:
        if combo.startswith(towel):
            total += is_combination_viable(combo.removeprefix(towel), towels)

    return total


def main():
    with open("input.txt") as f:
        towels = f.readline().strip().split(", ")
        f.readline()  # blank line
        combos = f.read().splitlines()

    towels = tuple(sorted(towels, key=len))

    part_1 = 0
    part_2 = 0

    for combo in combos:
        if result := is_combination_viable(combo, towels):
            part_1 += 1
            part_2 += result

    print("Part 1:", part_1)
    print("Part 2:", part_2)


if __name__ == "__main__":
    print(timeit(main, number=1))
