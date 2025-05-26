
def solution(A):
    if len(A) <= 1:
        return 0

    events = []
    for i in range(len(A)):
        left = i - A[i]
        right = i + A[i]
        events.append((left, 1, i))
        events.append((right, -1, i))

    events.sort(key=lambda x: (x[0], -x[1]))

    active_count = 0
    total_intersections = 0

    for pos, event_type, _ in events:
        if event_type == 1:
            total_intersections += active_count
            if total_intersections > 10_000_000:
                return -1
            active_count += 1
        else:
            active_count -= 1

    return total_intersections
