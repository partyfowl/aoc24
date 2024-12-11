from collections import Counter
from functools import cache
from timeit import timeit


@cache
def get_digits(value: int):
    count = 0
    while value:
        value //= 10
        count += 1
    return count


@cache
def process_stone(value: int) -> tuple[int] | tuple[int, int]:
    if value == 0:
        return (1,)

    length = get_digits(value)
    if length % 2 == 0:
        pow10 = 10 ** (length // 2)
        return divmod(value, pow10)

    return (value * 2024,)


def main():
    with open("input.txt") as f:
        counter = Counter(int(_) for _ in f.read().split(" "))

    for _ in range(75):
        step_counter = Counter()
        for value, count in counter.items():
            for processed in process_stone(value):
                step_counter[processed] += count
        counter = step_counter

    print(counter.total())


if __name__ == "__main__":
    print(timeit(main, number=1))
