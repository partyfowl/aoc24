from timeit import timeit


def is_combination_viable(combo: str, towels: list[str]):
    if combo == "":
        return True

    for towel in towels:
        if combo.startswith(towel):
            if is_combination_viable(combo.removeprefix(towel), towels):
                return True
    return False


def main():
    with open("input.txt") as f:
        towels = f.readline().strip().split(", ")
        f.readline()  # blank line
        combos = f.read().splitlines()

    towels = sorted(towels, key=len)

    towel_primitives = []

    # Check for towels that are formed of other towels, we don't need to use these
    for i, towel in enumerate(towels):
        if not is_combination_viable(towel, towels[:i]):
            towel_primitives.insert(0, towel)

    count = 0
    for combo in combos:
        if is_combination_viable(combo, towel_primitives):
            count += 1
    print(count)


if __name__ == "__main__":
    print(timeit(main, number=1))
