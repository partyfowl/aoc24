from collections import defaultdict, deque
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

    part_1_total = 0

    combo_cache = defaultdict(dict)

    for secret in secrets:
        key = secret
        price = secret % 10

        # Only track the last 4 price changes
        changes = deque(maxlen=combo_length)

        for i in range(1, iterations + 1):
            secret = evolve(secret)
            new_price = secret % 10
            change = new_price - price
            price = new_price
            changes.append(change)
            if i >= combo_length:
                # This list (deque) is maximum length 4
                combo = tuple(changes)
                if combo not in combo_cache[key]:
                    combo_cache[key][combo] = price

        part_1_total += secret

    combo_scores = defaultdict(int)

    for cache in combo_cache.values():
        for combo, price in cache.items():
            combo_scores[combo] += price

    print("Part 1:", part_1_total)
    print("Part 2:", max(combo_scores.values()))


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 5.714555202000156
