def solution(A):
    N = len(A)
    if N < 3:
        return 0

    A.sort()

    triplet_count = 0

    for R_idx in range(N - 1, 1, -1):
        P_idx = 0
        Q_idx = R_idx - 1

        while P_idx < Q_idx:
            if A[P_idx] + A[Q_idx] > A[R_idx]:
                triplet_count += (Q_idx - P_idx)
                Q_idx -= 1
            else:
                P_idx += 1

    return triplet_count
