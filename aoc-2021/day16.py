from functools import partial
import sys

sys.setrecursionlimit(10000)


table = {
    "0": "0000", "1": "0001", "2": "0010", "3": "0011",
    "4": "0100", "5": "0101", "6": "0110", "7": "0111",
    "8": "1000", "9": "1001", "A": "1010", "B": "1011",
    "C": "1100", "D": "1101", "E": "1110", "F": "1111",
}


b2d = partial(int, base=2)


def parse(input: str):
    return "".join(table[c] for c in input.strip())


bits = parse(open("input/day16.txt").read())


def parse_header(packet: str):
    return b2d(packet[:3]), b2d(packet[3:6])


def parse_literal(packet: str):
    ptr = 6
    blocks = []
    while True:
        blocks.append(packet[ptr+1:ptr+5])
        if packet[ptr] == "0":
            break
        ptr += 5

    num = "".join(blocks)
    # Return value and length of the packet in bits
    return b2d(num), 6 + len(num) + len(blocks)


def parse_packet(packet: str):
    v, t = parse_header(packet)
    vs = v
    value = 0

    if t == 4:
        # Return version, and the value with packet length
        return v, *parse_literal(packet)

    ptr = 7
    if packet[ptr - 1] == "0":
        nb = b2d(packet[ptr:ptr+15])
        ptr += 15
        # Strip excess bits.
        packet = packet[:ptr+nb]
        vals = []
        while ptr < len(packet):
            v, num, offset = parse_packet(packet[ptr:])
            vs += v
            ptr += offset
            vals.append(num)
    else:
        np = b2d(packet[ptr:ptr+11])
        ptr += 11
        vals = []
        for _ in range(np):
            v, num, offset = parse_packet(packet[ptr:])
            vs += v
            ptr += offset
            vals.append(num)

    match t:
        case 0:
            value = sum(vals)
        case 1:
            value = vals[0]
            for v in vals[1:]:
                value *= v
        case 2:
            value = min(vals)
        case 3:
            value = max(vals)
        case 5:
            value = 1 if vals[0] > vals[1] else 0
        case 6:
            value = 1 if vals[0] < vals[1] else 0
        case 7:
            value = 1 if vals[0] == vals[1] else 0
        case _:
            pass

    # Return version sum, value and offset for the pointer
    return vs, value, ptr


def part1():
    return parse_packet(bits)[0]


def part2():
    return parse_packet(bits)[1]
