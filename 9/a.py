import re
from timeit import timeit


def main():
    digit_re = re.compile(r"(\d)(\d)?")
    file_id = 0
    disk = []
    with open("input.txt") as f:
        while match := digit_re.match(f.read(2)):
            file_length, empty_space = (int(_) if _ else 0 for _ in match.groups())
            disk.extend([file_id] * file_length)
            disk.extend(["."] * empty_space)
            file_id += 1

    # defrag
    while "." in disk:
        try:
            disk[disk.index(".")] = disk.pop()
        except ValueError:
            pass

    total = 0
    for i, file_id in enumerate(disk):
        total += i * file_id

    print(total)


if __name__ == "__main__":
    print(timeit(main, number=1))
