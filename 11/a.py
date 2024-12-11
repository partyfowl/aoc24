from functools import cache
from timeit import timeit


@cache
def process_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    stone_str = str(stone)
    length = len(stone_str)
    if length % 2 == 0:
        mid = length // 2
        return [int(stone_str[:mid]), int(stone_str[mid:])]

    return [stone * 2024]


def main():
    with open("input.txt") as f:
        stones = [int(_) for _ in f.read().split(" ")]

    for _ in range(25):
        new_stones = []
        for stone in stones:
            new_stones.extend(process_stone(stone))
        stones = new_stones

    print(len(new_stones))


if __name__ == "__main__":
    print(timeit(main, number=1))
