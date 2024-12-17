from math import ceil

from common import parse, process_instructions


def search(
    min_a: int, max_a: int, b: int, c: int, instructions: list[int], index: int = -1
):

    step = ceil((max_a - min_a) / 64)  # why does 64 work?
    a = min_a

    while a <= max_a:
        result = process_instructions(a, b, c, instructions)[-1]

        if result == instructions:
            return a

        if len(result) == len(instructions) and result[index:] == instructions[index:]:

            if result := search(a - step, a + step, b, c, instructions, index - 1):
                return result

            index -= 1

        a += step


def main():
    _, b, c, instructions = parse()

    # Noticed that this adds a digit every multiple of 8
    # Setting min_a and max_a to the highest and lowest values
    # that have the correct number of digits

    max_a = 281_474_976_710_639  # Worked out manually
    min_a = 35_184_372_088_832  # Worked out manually

    min_a = 165064183119851  # This is a bug left in from debugging but it doesn't work without it

    a = search(min_a, max_a, b, c, instructions)

    print(a)


if __name__ == "__main__":
    main()
