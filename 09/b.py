import re
from timeit import timeit


def main():
    digit_re = re.compile(r"(\d)(\d)?")
    file_id = 0
    disk: list[tuple[int, int]] = []
    largest_empty_space = 0
    with open("input.txt") as f:
        while match := digit_re.match(f.read(2)):
            file_length, empty_space = (int(_) if _ else 0 for _ in match.groups())
            disk.append((file_id, file_length))
            disk.append((".", empty_space))
            largest_empty_space = max(largest_empty_space, empty_space)
            file_id += 1

    # disk[-2::-2] creates a copy of the list, reversed, and gets every other value via slice
    # In this case, we get only the files, not the blank space
    for file in disk[-2::-2]:
        file_index = disk.index(file)
        file_id, file_length = file

        for i in range(file_index):
            loop_file_id, loop_file_length = disk[i]
            if loop_file_id == ".":
                if loop_file_length == file_length:
                    # Swap positions of blank space and empty file
                    disk[file_index], disk[i] = disk[i], disk[file_index]
                    break
                elif loop_file_length > file_length:
                    # Space created by moved file
                    disk[file_index] = (".", file_length)

                    # Space leftover after moved file is inserted
                    disk[i] = (".", loop_file_length - file_length)

                    # Insert the file before the space
                    disk.insert(i, file)
                    break

    total = 0
    index = 0

    for file_id, file_length in disk:
        for i in range(file_length):
            if file_id != ".":
                total += file_id * index
            index += 1

    print(total)


if __name__ == "__main__":
    print(timeit(main, number=1))
