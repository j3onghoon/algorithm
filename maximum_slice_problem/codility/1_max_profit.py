
def solution(A):
    N = len(A)
    if N == 0:
        return 0

    min_value = A[0]
    max_profit = 0
    for i in range(1, N):
        if min_value > A[i]:
            min_value = A[i]
        else:
            max_profit = max(max_profit, A[i] - min_value)

    return max_profit