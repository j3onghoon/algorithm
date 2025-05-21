"""
문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
입출력 예
tickets	return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

"""

from collections import defaultdict


def solution_dfs(tickets):
    graph = defaultdict(list)

    for fr, to in tickets:
        graph[fr].append(to)

    for airport in graph:
        graph[airport].sort()

    route = ["ICN"]
    N = len(tickets)

    def dfs():
        if len(route) == N + 1:
            return True

        airport = route[-1]

        if airport not in graph and not graph[airport]:
            return False

        for idx, to in enumerate(graph[airport]):
            graph[airport].pop(idx)
            route.append(to)

            if dfs():
                return True

            route.pop(to)
            graph[airport].insert(idx, to)

        return False

    dfs()
    return route


def solution_stack(tickets):
    graph = defaultdict(list)

    for idx, (fr, to) in enumerate(tickets):
        graph[fr].append((to, idx))

    for airport in graph:
        graph[airport].sort()

    stack = [("ICN", ["ICN"], set())]
    N = len(tickets)

    while stack:
        fr, path, used = stack.pop()

        if len(used) == N:
            return path

        for to, idx in reversed(graph[fr]):
            if (fr, to, idx) not in used:
                new_used = used.copy()
                new_used.add((fr, to, idx))
                new_path = path + [to]
                stack.append((to, new_path, new_used))
