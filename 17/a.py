from common import parse, process_instructions


def main():
    a, b, c, instructions = parse()

    result = ",".join(str(_) for _ in process_instructions(a, b, c, instructions)[-1])

    print(result)


if __name__ == "__main__":
    main()
