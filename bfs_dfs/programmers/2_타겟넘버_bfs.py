from collections import deque


def solution(numbers, target):
    answer = 0

    queue = deque([(0, 0)])
    N = len(numbers)
    while queue:
        current_sum, next_idx = queue.popleft()

        if next_idx == N and current_sum == target:
            answer += 1
        else:
            queue.append((current_sum + numbers[next_idx], next_idx + 1))
            queue.append((current_sum - numbers[next_idx], next_idx + 1))
    return answer


















"""
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

"""