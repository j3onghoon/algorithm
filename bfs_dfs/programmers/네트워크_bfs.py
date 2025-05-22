from collections import deque


def solution(n, computers):
    def bfs(start, visited):
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()

            for neighbor in range(n):
                if computers[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    visited = [False] * n
    network_count = 0

    for node in range(n):
        if not visited[node]:
            bfs(node, visited)
            network_count += 1

    return network_count