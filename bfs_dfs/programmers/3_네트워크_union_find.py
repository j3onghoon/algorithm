






















"""
union-find 알고리즘에서 rank는 최적화에 사용된다.

rank없이 수행하면 트리가 한쪽으로 치우쳐 연결리스트처럼 되어 O(N)이 될 수 있다.
rank를 사용하면 O(log n)
rank + 경로압축


def solution(n, computers):
    def find_parent(parent, x):
        return parent[x] if parent[x] == x else find_parent(parent, parent[x])

    def union_nodes(parent, rank, a, b):
        root_a = find_parent(parent, a)
        root_b = find_parent(parent, b)

        if root_a == root_b:
            return

        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            if rank[root_a] == rank[root_b]:
                rank[root_a] += 1

    parent = [i for i in range(n)]
    rank = [0] * n

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union_nodes(parent, rank, i, j)

    unique_networks = set()
    for i in range(n):
        unique_networks.add(find_parent(parent, i))

    return len(unique_networks)
"""