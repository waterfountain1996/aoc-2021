from collections import Counter


def parse(input: list[str]):
    entries = [line.split(" | ") for line in input]
    patterns = [p.split() for p, _ in entries]
    outputs = [o.split() for _, o in entries]
    return patterns, outputs


data = parse(open("input/day08.txt").readlines())


def part1():
    nums = [x for y in data[1] for x in y]
    cc = Counter([''.join(sorted(num)) for num in nums])
    return sum(v for k, v in cc.items() if len(k) in (2, 3, 4, 7))


DIGIT_TO_CONF = {
    0: (0, 1, 4, 6, 5, 2),
    1: (1, 4),
    2: (0, 1, 3, 5, 6),
    3: (0, 1, 3, 4, 6),
    4: (1, 2, 3, 4),
    5: (0, 2, 3, 4, 6),
    6: (0, 2, 3, 4, 5, 6),
    7: (0, 1, 4),
    8: (0, 1, 2, 3, 4, 5, 6),
    9: (0, 1, 2, 3, 4, 6),
}

def digits_from_config(config: list[str]) -> list[str]:
    digits = []
    for v in DIGIT_TO_CONF.values():
        sd = "".join(c for i,c in enumerate(config) if i in v)
        sd = "".join(sorted(sd))
        digits.append(sd)
    return digits


def find_config(patterns: list[str]):
    fives = [p for p in patterns if len(p) == 5]    # 2, 3, 5
    sixes = [p for p in patterns if len(p) == 6]    # 6 9 0
    fives_common = set(fives[0]) & set(fives[1]) & set(fives[2])
    sixes_common = set(sixes[0]) & set(sixes[1]) & set(sixes[2])

    config = ['.'] * 7
    one = [p for p in patterns if len(p) == 2].pop()
    four = [p for p in patterns if len(p) == 4].pop()
    seven = [p for p in patterns if len(p) == 3].pop()

    # Top segment is in 7 but not in one.
    config[0] = [c for c in seven if c not in one].pop()
    # Bottom right is present in 6, 9, 0 and in one.
    config[4] = [c for c in sixes_common if c in one].pop()
    # Top right from one that is not a bottom right.
    config[1] = [c for c in one if c != config[4]].pop()
    # 4 and 2, 3, 5 only have middle segment in common.
    config[3] = [c for c in fives_common & set(four)].pop()
    # Top left is the only segment from 4 that we haven't defined yet
    config[2] = [c for c in four if c not in config].pop()
    # Bottom is common between 0 2 3 5 9 0.
    config[6] = [c for c in fives_common & sixes_common if c != config[0]].pop()
    # The last missing segment.
    config[5] = [c for c in "abcdefg" if c not in config].pop()
    return config


def part2():
    total = 0
    for i, patterns in enumerate(data[0]):
        config = find_config(patterns)
        digits = digits_from_config(config)
        output = ["".join(sorted(n)) for n in data[1][i]]
        num = int("".join(str(digits.index(d)) for d in output))
        total += num
    return total
