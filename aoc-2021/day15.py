import heapq


def parse(input: str):
    return [[int(x) for x in row] for row in input.splitlines(False)]


risk_map = parse(open("input/day15.txt").read().strip())


def neighbours(i, j, risk_map):
    yield (i, j + 1) if j + 1 < len(risk_map[i]) else None
    yield (i + 1, j) if i + 1 < len(risk_map) else None
    yield (i, j - 1) if j - 1 >= 0 else None
    yield (i - 1, j) if i - 1 >= 0 else None


def weight(initial: int, tile: tuple[int, int]):
    if initial < 10:
        return initial

    return initial + sum(tile) - 9


def dijkstra(s, risk_map, tile = (0, 0)):
    visited = set()
    dst = {}
    q = [(0, s)]
    while q:
        w, node = heapq.heappop(q)
        ns = [n for n in neighbours(node[0], node[1], risk_map)
              if n is not None and n not in visited]
        for n in ns:
            tmp = w + weight(risk_map[n[0]][n[1]], tile)
            if n not in dst or dst[n] > tmp:
                dst[n] = tmp
                heapq.heappush(q, (dst[n], n))
        visited.add(node)
    return dst


def part1():
    distances = dijkstra((0, 0), risk_map)
    size = len(risk_map)
    return distances[(size-1, size-1)]


def part2():
    # TODO: Optimize
    global risk_map

    # Increase to the right
    for i in range(1, 5):
        incr = [[x+i if x+i < 10 else x+i-9 for x in row[:len(risk_map)]] for row in risk_map]
        for j, row in enumerate(incr):
            risk_map[j].extend(row)

    # Increase downwards
    incrs = []
    for i in range(1, 5):
        incr = [[x+i if x+i < 10 else x+i-9 for x in row] for row in risk_map]
        incrs.append(incr)

    for row in incrs:
        risk_map.extend(row)

    # Now count
    distances = dijkstra((0, 0), risk_map)
    size = len(risk_map)
    return distances[(size-1, size-1)]
