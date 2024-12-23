import re
import time
from collections import Counter
from itertools import product
from timeit import timeit


def check_connection(a: Counter[str], b: Counter[str], c: Counter[str]):
    this = a + b + c
    if set(this.values()) == {2}:
        return ",".join(sorted((this.keys())))


def main():
    regex = re.compile(r"(\w\w)-(\w\w)")
    connections: list[Counter[str]] = []
    connections_t: list[Counter[str]] = []
    with open("input.txt") as f:
        for a, b in regex.findall(f.read()):
            counter = Counter((a, b))
            connections.append(counter)
            if a.startswith("t") or b.startswith("t"):
                connections_t.append(counter)

    answer = set()

    start = time.time()

    for i, (a, b, c) in enumerate(product(connections_t, connections_t, connections)):

        this = a + b + c

        if set(this.values()) == {2}:
            answer.add(",".join(sorted((this.keys()))))

        if i % 1000000 == 0:  # Effectively a progress bar
            print(i, round(time.time() - start, 2))

    print(len(answer))


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 1528 seconds == 25 minutes 28 seconds
