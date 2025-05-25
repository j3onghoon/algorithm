from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(maps):
    return find_shortest_path(maps)

def find_shortest_path(maps):
    len_col = len(maps)
    len_row = len(maps[0])

    visited = [[-1] * len_row for _ in range(len_col)]

    queue = deque([(0, 0)])
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()

        if x == len_row - 1 and y == len_col - 1:
            return visited[y][x]

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if is_movable(nx, ny, len_col, len_row, maps, visited):
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))

    return -1

def is_movable(x, y, len_col, len_row, maps, visited):
    return (0 <= x < len_row and
            0 <= y < len_col and
            maps[y][x] == 1 and
            visited[y][x] == -1)












"""
from collections import deque


def solution(maps):
    rows, cols = len(maps), len(maps[0])

    target = (rows - 1, cols - 1)

    visited = [[-1 for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = 1

    return find_shortest_path(maps, visited, target)

def find_shortest_path(maps, visited, target):
    rows, cols = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) == target:
            return visited[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if is_valid_move(nx, ny, rows, cols, maps, visited):
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return -1

def is_valid_move(x, y, rows, cols, maps, visited):
    return (0 <= x < rows and
            0 <= y < cols and
            maps[x][y] == 1 and
            visited[x][y] == -1)

"""