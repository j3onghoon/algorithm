





















"""
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[-1] * 102 for _ in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = [i * 2 for i in r]

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[j][i] = 0
                elif field[j][i] != 0:
                    field[j][i] = 1


    return find_shortest_path(field, characterX * 2, characterY * 2, itemX * 2, itemY * 2)

def find_shortest_path(field, characterX, characterY, itemX, itemY):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([(characterX, characterY)])
    visited = [[-1] * 102 for _ in range(102)]
    visited[characterY][characterX] = 0

    while queue:
        x, y = queue.popleft()
        if x == itemX and y == itemY:
            return visited[y][x] / 2

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102 and field[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))
    return -1



# 2배 확장으로 풀기
#
# def solution(rectangle, characterX, characterY, itemX, itemY):
#     field = [[-1] * 102 for _ in range(102)]
#
#     for r in rectangle:
#         x1, y1, x2, y2 = r
#         x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
#
#         for i in range(x1, x2 + 1):
#             for j in range(y1, y2 + 1):
#                 if x1 < i < x2 and y1 < j < y2:
#                     field[i][j] = 0
#                 elif field[i][j] != 0:
#                     field[i][j] = 1
#
#     characterX, characterY = characterX * 2, characterY * 2
#     itemX, itemY = itemX * 2, itemY * 2
#
#     q = deque([(characterX, characterY, 0)])
#     visited = [[False] * 102 for _ in range(102)]
#     visited[characterX][characterY] = True
#
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#
#     while q:
#         x, y, dist = q.popleft()
#         if x == itemX and y == itemY:
#             return dist // 2
#
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#
#             if 0 <= nx < 102 and 0 <= ny < 102 and field[nx][ny] == 1 and not visited[nx][ny]:
#                 q.append((nx, ny, dist + 1))
#                 visited[nx][ny] = True
#
#     return -1
"""