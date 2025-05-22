from collections import deque


def solution(game_board, table):
    # 1. 0을 찾는다.
    # 2. 0을 기준으로 1이 나올 때까지를 찾는다. 도형 찾기
    # 3. 도형을 복사해온다. 기존 도형은 1로 채운다.
    # 4. 해당 리스트가 table에 있는지 확인한다.
    # 5. 직사각형을 돌려가며 찾는다.
    # 6. 직사각형이 table에 있다면 칸 수만큼 +한다.

    n = len(game_board)
    answer = 0

    spaces = find_blocks(game_board, 0)
    pieces = find_blocks(table, 1)
    used = [False] * len(pieces)

    for space in spaces:
        for i, piece in enumerate(pieces):
            if used[i]:
                continue

            if len(space) != len(piece):
                continue

            if can_match(space, piece):
                answer += len(piece)
                used[i] = True
                break

    return answer


def find_blocks(board, target):
    n = len(board)
    visited = [[False] for _ in range(n) for _ in range(n)]
    blocks = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == target and not visited[i][j]:
                block = []
                queue = deque([(i, j)])
                visited[i][j] = True

                while queue:
                    x, y = queue.popleft()
                    block.append((x, y))

                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
                            queue.append((nx, ny))
                            visited[nx][ny] = True

                blocks.append(normalize(block))

    return blocks

def normalize(block):
    min_x = min(x for x, y in block)
    min_y = min(y for x, y in block)

    return {(x - min_x, y - min_y) for x, y in block}

def rotate(block):
    rotated = [(y, -x) for x, y in block]
    return normalize(rotated)

def can_match(space, piece):
    rotated = piece
    for _ in range(4):
        if rotated == space:
            return True
        rotated = rotate(rotated)
    return False
