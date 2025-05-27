"""
Dynamic Programming
"""

def solution(A):
    n = len(A)
    if n < 3:
        return 0

    max_left = [0] * n
    for i in range(1, n - 1):
        max_left[i] = max(0, max_left[i - 1] + A[i])

    max_right = [0] * n
    for i in range(n - 2, 0, -1):
        max_right[i] = max(0, max_right[i + 1] + A[i])

    return max(max_left[y - 1] + max_right[y + 1] for y in range(1, n - 1))


def solution_optimized(A):
    n = len(A)
    if n < 3:
        return 0

    max_left = [0] * n
    max_right = [0] * n

    current_sum = 0
    for i in range(1, n - 1):
        current_sum = max(0, current_sum + A[i])
        max_left[i] = current_sum

    current_sum = 0
    for i in range(n - 2, 0, -1):
        current_sum = max(0, current_sum + A[i])
        max_right[i] = current_sum

    result = 0
    for y in range(1, n - 1):
        result = max(result, max_left[y - 1] + max_right[y + 1])

    return result
