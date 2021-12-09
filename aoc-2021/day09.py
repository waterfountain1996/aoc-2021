from collections import deque


def parse(input: list[str]) -> list[list[int]]:
    return [[int(n) for n in list(line)] for line in input] 


data = parse([x.strip() for x in open("input/day09.txt").readlines()])


def adjacent(i: int, j: int, board: list[list[int]]):
    yield (i+1, j) if i+1 < len(board) else None
    yield (i-1, j) if i-1 >= 0 else None
    yield (i, j+1) if j+1 < len(board[i]) else None
    yield (i, j-1) if j-1 >= 0 else None


def is_low(i: int, j: int, board: list[list[int]]):
    return all(board[adj[0]][adj[1]] > board[i][j]
               for adj in adjacent(i, j, data) if adj is not None)


def part1():
    total = 0 
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            total = total + col + 1 if is_low(i, j, data) else total
    return total


def bfs(i, j, board, seen, dq, size=0):
    if (i, j) in seen:
        return size

    cc = list(adj for adj in adjacent(i, j, data)
              if adj is not None
              and board[adj[0]][adj[1]] != 9
              and board[adj[0]][adj[1]] > board[i][j])

    dq.extend(cc)
    while dq:
        x, y = dq.popleft()
        seen.add((i, j))
        size += bfs(x, y, board, seen, dq, size)

    return size + 1


def part2():
    biggest = []
    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            if is_low(i, j, data):
                basin = bfs(i, j, data, set(), deque())
                if not biggest or basin >= min(biggest):
                    biggest.append(basin)
                    if len(biggest) > 3:
                        biggest.sort()
                        biggest.pop(0)
    return biggest[0] * biggest[1] * biggest[2]
