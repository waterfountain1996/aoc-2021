from collections import Counter


with open("input/day03.txt") as f:
    report = [x.strip() for x in f.readlines()]


def part1():
    bits = [
        Counter(map(lambda x: x[i], report)).most_common(2)
        for i in range(len(report[0]))
    ]
    gamma = int(''.join(bit[0][0] for bit in bits), base=2)
    epsilon = int(''.join(bit[1][0] for bit in bits), base=2)
    return gamma * epsilon


def rating_filter(report: list[str], most_common: bool) -> str:
    num = ""
    for i in range(len(report[0])):
        report = [n for n in report if n.startswith(num)]
        if len(report) == 1:
            break

        cc = Counter(map(lambda x: x[i], report)).most_common(2)
        nc = cc[0][0] if most_common else cc[1][0]
        if cc[0][1] == cc[1][1]:
            nc = "1" if most_common else "0"

        num += nc

    return report[0]



def part2():
    oxygen = rating_filter(report.copy(), most_common=True)
    co2 = rating_filter(report.copy(), most_common=False)
    return int(oxygen, base=2) * int(co2, base=2)
