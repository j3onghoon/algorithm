def solution(A):
    min_difference = float('inf')
    total_sum = sum(A)

    left_sum = 0
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum

        min_difference = min(min_difference, abs(left_sum - right_sum))
    return min_difference
