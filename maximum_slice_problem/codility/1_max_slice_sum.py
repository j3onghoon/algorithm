def solution(A):
    if not A:
        return 0

    total_max = A[0]
    current_max = A[0]

    for i in range(1, len(A)):
        current_max = max(A[i], current_max + A[i])
        total_max = max(total_max, current_max)

    return total_max
