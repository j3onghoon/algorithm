def solution(A):
    N = len(A)

    A.sort()

    left = 0
    right = N - 1

    min_abs_sum = 2000000001

    while left <= right:
        current_sum = A[left] + A[right]

        if current_sum == 0:
            return 0

        min_abs_sum = min(min_abs_sum, abs(current_sum))

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return min_abs_sum
