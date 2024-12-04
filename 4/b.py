with open("input.txt") as f:
    grid = f.read().split("\n")

diagonals = {"M", "S"}
total = 0

for y in range(1, len(grid)):
    for x in range(1, len(grid[0])):
        if grid[x][y] == "A":
            try:
                if (
                    {grid[x + 1][y + 1], grid[x - 1][y - 1]}
                    == {grid[x - 1][y + 1], grid[x + 1][y - 1]}
                    == diagonals
                ):
                    total += 1
            except IndexError:
                pass

print(total)
