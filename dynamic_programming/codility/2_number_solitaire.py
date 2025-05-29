def solution(A):
    N = len(A)

    if N <= 1:
        return A[0]

    dp = [0] * 6
    dp[0] = A[0]

    for i in range(1, min(N, 6)):
        prev_max = max(dp[0:i])
        dp[i] = prev_max + A[i]

    for i in range(6, N):
        prev_max = max(dp)
        dp[i % 6] = prev_max + A[i]

    return dp[(N - 1) % 6]
