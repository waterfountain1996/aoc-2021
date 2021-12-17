def parse(input: str):
    limits = input.removeprefix("target area: ").split(", ")
    limits = [x[2:].split("..") for x in limits]
    limits = tuple((int(x[0]), int(x[1])) for x in limits)
    limits = tuple(abs(x) for x in limits[0]), limits[1]
    return limits


def reaches(vx, vy, target):
    tx = max(abs(x) for x in target[0])
    ty = min(target[1])
    x = y = 0
    while x <= tx and y >= ty:
        x += vx
        y += vy
        vy -= 1
        if vx != 0: vx -= 1
        if (
            x in range(min(target[0]), max(target[0])+1) and 
            y in range(min(target[1]), max(target[1])+1)
        ):
            return True
    return False


def solve():
    target = parse(open("input/day17.txt").read().strip())
    mxx, mxy = max(target[0]), min(target[1])
    mnx = 0
    while sum(range(mnx+1)) < min(target[0]):
        mnx += 1

    highest = i = 0
    for x in range(mnx, mxx+1):
        for y in reversed(range(mxy, abs(min(target[1])))):
            if reaches(x, y, target):
                i += 1
                if (y := sum(range(abs(y)))) > highest:
                    highest = y
    return highest, i


def part1():
    return solve()[0]


def part2():
    return solve()[1]
