def solution(A, B):
    N = len(A)

    if N == 0:
        return 0

    count = 1

    last_end_point = B[0]

    for i in range(1, N):
        if A[i] > last_end_point:
            count += 1
            last_end_point  = B[i]

    return count
