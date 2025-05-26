def solution(A):
    A.sort()

    candidate_1 = A[0] * A[1] * A[-1]
    candidate_2 = A[-3] * A[-2] * A[-1]
    return max(candidate_1, candidate_2)
