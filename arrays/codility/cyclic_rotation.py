def solution(A, K):
    if not A:
        return []
    point = K % len(A)
    return A[-point:] + A[:-point]
