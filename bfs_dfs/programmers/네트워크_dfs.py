def solution(n, computers):
    def dfs(node, visited):
        visited[node] = True

        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor, visited)

    visited = [False] * n
    network_count = 0

    for node in range(n):
        if not visited[node]:
            dfs(node, visited)
            network_count += 1

    return network_count
