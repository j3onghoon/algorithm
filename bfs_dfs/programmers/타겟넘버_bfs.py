from collections import deque


def solution(numbers, target):
    N = len(numbers)
    q = deque([(0, 0)])
    count = 0

    while q:
        idx, current_sum = q.popleft()

        if idx == N:
            if current_sum == target:
                count += 1
        else:
            q.append((idx + 1, current_sum + numbers[idx]))
            q.append((idx + 1, current_sum - numbers[idx]))

    return count