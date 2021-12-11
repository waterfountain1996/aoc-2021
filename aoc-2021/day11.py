with open("input/day11.txt") as f:
    data = [[int(x) for x in list(line.strip())] for line in f.readlines()]


def adjacent(i: int, j: int, grid: list[list[int]]):
    yield (i+1, j) if i+1 < len(grid) else None
    yield (i-1, j) if i-1 >= 0 else None
    yield (i, j+1) if j+1 < len(grid[i]) else None
    yield (i, j-1) if j-1 >= 0 else None
    yield (i+1, j+1) if i+1 < len(grid) and j+1 < len(grid[i]) else None
    yield (i+1, j-1) if i+1 < len(grid) and j-1 >= 0 else None
    yield (i-1, j-1) if i-1 >= 0 and j-1 >= 0 else None
    yield (i-1, j+1) if i-1 >= 0 and j+1 < len(grid[i]) else None


def flash(grid, seen=None):
    if seen is None:
        seen = set()

    flashed = [x for x in get_flashed(grid) if x not in seen]
    seen.update(flashed)

    if not (affected := list(
        x for i, j in flashed
        for x in adjacent(i, j, grid)
        if x is not None and grid[x[0]][x[1]] < 10
    )):
        return

    for x, y in affected:
        grid[x][y] += 1

    flash(grid, seen)


def get_flashed(grid):
    return list(
        (i, j) for i, row in enumerate(grid)
        for j, _ in enumerate(row) if grid[i][j] > 9
    )
    

def part1(octopuses = data.copy()):
    total = 0
    for _ in range(100):
        octopuses = [[x + 1 for x in row] for row in octopuses]
        flash(octopuses)

        for i, j in get_flashed(octopuses):
            total += 1
            octopuses[i][j] = 0

    return total


def part2(octopuses = data.copy()):
    step = 0
    while True:
        step += 1
        octopuses = [[x + 1 for x in row] for row in octopuses]
        flash(octopuses)

        flashed = get_flashed(octopuses)
        if len(flashed) == 100:
            return step

        for i, j in flashed:
            octopuses[i][j] = 0
