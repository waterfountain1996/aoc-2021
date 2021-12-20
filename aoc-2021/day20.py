def parse(input: str):
    algo, img = input.split("\n\n")
    img = [list(x) for x in img.splitlines(False)]
    img = {(i, j): img[i][j] for i in range(len(img)) for j in range(len(img))}
    return algo, img


def box(i, j):
    yield i-1, j-1
    yield i-1, j
    yield i-1, j+1
    yield i, j-1
    yield i, j
    yield i, j+1
    yield i+1, j-1
    yield i+1, j
    yield i+1, j+1


algo, img = parse(open("input/day20.txt").read().strip())


def add_padding(img, pad=2):
    img = [['.'] * len(img[0])] * pad + img
    img = img + [['.'] * len(img[0])] * pad 
    img = [['.'] * pad + line + ['.'] * pad for line in img]
    return img


def count_lit(img):
    return sum(1 for row in img for c in row if c == "#")


def enhance(algo, input, chr):
    size = int(len(input) ** (1/2))
    output = {}
    for i in range(-1, size + 1):
        for j in range(-1, size + 1):
            pixels = "".join(input.get(x, chr) for x in box(i, j))
            bn = pixels.translate({35: 49, 46: 48})
            output[i + 1, j + 1] = algo[int(bn, base=2)]
    return output


def solve(steps):
    output = img
    for i in range(1, steps+1):
        output = enhance(algo, output, '#' if i % 2 == 0 else '.')
    return sum(1 for v in output.values() if v == "#")


def part1():
    return solve(2)


def part2():
    return solve(50)
