# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, M, A):
    n = len(A)

    if K >= n:
        return max(A)

    if K == 1:
        return sum(A)

    left = max(A)
    right = sum(A)

    while left < right:
        mid = (left + right) // 2

        if can_divide(A, K, mid):
            right = mid
        else:
            left = mid + 1

    return left


def can_divide(A, K, max_sum):
    current_sum = 0
    blocks_used = 1

    for num in A:
        if current_sum + num <= max_sum:
            current_sum += num
        else:
            blocks_used += 1
            current_sum = num

            if blocks_used > K:
                return False

    return True
