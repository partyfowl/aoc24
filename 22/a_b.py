from collections import defaultdict
from timeit import timeit


def mix_and_prune(secret: int, other_number: int):
    secret ^= other_number
    secret %= 16777216
    return secret


def evolve(secret: int):
    secret = mix_and_prune(secret, secret * 64)
    secret = mix_and_prune(secret, secret // 32)
    secret = mix_and_prune(secret, secret * 2048)
    return secret


def main():
    with open("input.txt") as f:
        secrets = [int(_) for _ in f]

    iterations = 2000
    combo_length = 4

    changes = defaultdict(list)
    prices = defaultdict(list)

    part_1_total = 0

    for secret in secrets:
        key = secret
        price = secret % 10

        for _ in range(iterations):
            secret = evolve(secret)
            change = secret % 10 - price
            price = secret % 10
            changes[key].append(change)
            prices[key].append(price)

        part_1_total += secret

    possible_combos: set[tuple[int, int, int, int]] = set()

    for secret, secret_changes in changes.items():
        for n in range(1, 10):
            possible_combos.update(
                tuple(secret_changes[i - combo_length + 1 : i + 1])
                for i, x in enumerate(secret_changes)
                if x == n and i >= 3
            )

    combo_scores = defaultdict(int)

    for secret, secret_changes in changes.items():
        this_combos = possible_combos.copy()
        for i in range(combo_length, iterations):
            combo = tuple(secret_changes[i + 1 - combo_length : i + 1])
            if combo in this_combos:
                combo_scores[combo] += prices[secret][i]
                this_combos.remove(combo)

    print("Part 1:", part_1_total)
    print("Part 2:", max(combo_scores.values()))


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 8.890626477000296
