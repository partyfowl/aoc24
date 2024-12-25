from collections import defaultdict
from itertools import product


def main():
    with open("input.txt") as f:
        keys_locks = f.read().split("\n\n")

    keys = []
    locks = []

    for key_or_lock in keys_locks:
        heights = defaultdict(int)
        index = 0
        for i in key_or_lock:
            if i == "#":
                heights[index] += 1
            elif i == "\n":
                index = 0
                continue

            index += 1

        if key_or_lock.startswith("#"):
            locks.append(heights)
        else:
            keys.append(heights)
    total = 0

    for key, lock in product(keys, locks):
        for i, v in key.items():
            if lock[i] + v > 7:
                print("no match")
                break
        else:  # nobreak
            total += 1
    print(total)


if __name__ == "__main__":
    main()
