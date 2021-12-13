def parse(input: str):
    dots, folds = input.split("\n\n")
    dots = [line.split(",") for line in dots.splitlines(False)]
    dots = [(int(y), int(x)) for x, y in dots]
    folds = [line.split("=") for line in folds.splitlines(False)]
    folds = [(axis[-1], int(n)) for axis, n in folds]
    return dots, folds


dots, folds = parse(open("input/day13.txt").read())


def print_letters(matrix):
    for row in matrix:
        for c in row:
            print("OO" if c == "#" else "  ", end="")
        print()


def fx(dots, x):
    left = {dot for dot in dots if dot[1] < x}
    right = {(dot[0], x - (dot[1] - x)) for dot in dots if dot[1] > x}
    return left | right


def fy(dots, y):
    up = {dot for dot in dots if dot[0] < y}
    bottom = {(y - (dot[0] - y), dot[1]) for dot in dots if dot[0] > y}
    return up | bottom


def fold(dots, folds):
    for axis, n in folds:
        func = globals()[f"f{axis}"]
        dots = func(dots, n)
    return dots


def part1():
    return len(fold(dots, folds[:1]))


def part2():
    folded = fold(dots, folds)

    h, w = max(y for y, _ in folded) + 1, max(x for _, x in folded) + 1
    matrix = [['.'] * w for _ in range(h)]
    for x, y in folded:
        matrix[x][y] = '#'

    print_letters(matrix)
