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