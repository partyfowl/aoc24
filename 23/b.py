import re
from collections import defaultdict
from timeit import timeit


def main():
    regex = re.compile(r"(\w\w)-(\w\w)")

    connections: defaultdict[str, set[str]] = defaultdict(set)

    with open("input.txt") as f:
        for a, b in regex.findall(f.read()):
            connections[a].add(a)
            connections[a].add(b)
            connections[b].add(a)
            connections[b].add(b)

    longest = set()

    for computer in connections:
        network = {computer}
        for computer, computer_connections in connections.items():
            if all(_ in computer_connections for _ in network):
                network.add(computer)
        if len(network) > len(longest):
            longest = network

    print(",".join(sorted(longest)))


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 0.11799285100005363 seconds
