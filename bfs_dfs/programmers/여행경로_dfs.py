from collections import defaultdict


def solution(tickets):
    routes = defaultdict(dict)
    for departure, arrival in tickets:
        routes[departure][arrival] = routes[departure].get(arrival, 0) + 1

    path = ["ICN"]
    find_path(routes, "ICN", len(tickets), path)

    return path

def find_path(routes, current, remaining_tickets, path):
    if remaining_tickets == 0:
        return True

    if current not in routes:
        return False

    destinations = sorted(routes[current].keys())

    for next_airport in destinations:
        if routes[current][next_airport] > 0:
            routes[current][next_airport] -= 1
            path.append(next_airport)

            if find_path(routes, next_airport, remaining_tickets - 1, path):
                return True

            path.pop()
            routes[current][next_airport] += 1

    return False