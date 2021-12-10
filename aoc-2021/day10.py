input = [x.strip() for x in open("input/day10.txt").readlines()]


BLOCK_TABLE = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def is_opening(c: str) -> bool:
    return c in BLOCK_TABLE


def closes(c: str, opening: str) -> bool:
    return BLOCK_TABLE[opening] == c


def part1():
    table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    illegal = []
    for line in input:
        stack = []
        for c in line:
            if is_opening(c):
                stack.append(c)
            elif not closes(c, stack.pop()):
                illegal.append(c)
    return sum(map(table.__getitem__, illegal))


def part2():
    table = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for line in input:
        stack = []
        corrupted = False
        for c in line:
            if is_opening(c):
                stack.append(c)
            elif not closes(c, stack.pop()):
                corrupted = True
                break

        if not corrupted:
            score = 0
            for x in reversed([BLOCK_TABLE[x] for x in stack]):
                score = score * 5 + table[x]
            scores.append(score)

    scores.sort()
    return scores[len(scores) // 2]
