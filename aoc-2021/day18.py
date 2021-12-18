from copy import deepcopy
from itertools import permutations
from math import floor, ceil


def parse(input: str):
    return [eval(x) for x in input.splitlines(False)]


nums = parse(open("input/day18.txt").read())


def add(a, b):
    return [a, b]


def add_first_left(n, m):
    if isinstance(n[0], int):
        n[0] += m
    else:
        n[0] = add_first_left(n[0], m)
    return n


def add_first_right(n, m):
    if isinstance(n[1], int):
        n[1] += m
    else:
        n[1] = add_first_right(n[1], m)
    return n

def explode(num, level = 0, found = False):

    if level == 4 and isinstance(num, list):
        return 0, True, num[0], num[1]

    left = right = None

    if isinstance(num[0], list) and not found:
        res, found, left, right = explode(num[0], level+1, found)
        if found:
            if res == 0:
                num[0] = 0
            if right is not None:
                if isinstance(num[1], int):
                    num[1] += right
                else:
                    num[1] = add_first_left(num[1], right)
                right = None

    if isinstance(num[1], list) and not found:
        res, found, left, right = explode(num[1], level+1, found)
        if found:
            if res == 0:
                num[1] = 0
            if left is not None:
                if isinstance(num[0], int):
                    num[0] += left
                else:
                    num[0] = add_first_right(num[0], left)
                left = None

    return num, found, left, right


def split(n, found = False):
    if not found:
        if isinstance(n[0], list):
            n[0], found = split(n[0], found)
        elif n[0] > 9:
            n[0] = [floor(n[0] / 2), ceil(n[0] / 2)]
            return n, True

    if not found:
        if isinstance(n[1], list):
            n[1], found = split(n[1], found)
        elif n[1] > 9:
            n[1] = [floor(n[1] / 2), ceil(n[1] / 2)]
            return n, True

    return n, found


def reduce(n):
    while True:
        n, exploded, *_ = explode(n)
        if exploded:
            continue
        n, been_split = split(n)
        if been_split:
            continue
        break
    return n


def magnitude(n):
    if isinstance(n, int):
        return n

    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])


def sum_up(nums):
    n, *rest = nums
    for r in rest:
        n = reduce(add(n, r))
    return n


def part1():
    return magnitude(sum_up(nums))


def part2():
    return max(magnitude(reduce(add(deepcopy(a), deepcopy(b))))
               for a, b in permutations(nums, 2))
