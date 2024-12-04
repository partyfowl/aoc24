with open("input.txt") as f:
    grid = f.read().split("\n")

directions: list[tuple[int, int]] = []
for x in (-1, 0, 1):
    for y in (-1, 0, 1):
        if x or y:  # ignore (0, 0)
            directions.append((x, y))


word = "XMAS"
total = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        for dx, dy in directions:
            for i, char in enumerate(word):
                try:
                    cx = x + i * dx
                    cy = y + i * dy
                    if cx < 0 or cy < 0:
                        break
                    if grid[cx][cy] != char:
                        break
                except IndexError:
                    break
            else:  # nobreak
                total += 1

print(total)
