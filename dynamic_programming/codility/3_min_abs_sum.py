def solution(A):
    N = len(A)
    if N == 0:
        return 0

    total_sum = 0
    max_val = 0
    counts = [0] * 101

    for i in range(N):
        val = abs(A[i])
        counts[val] += 1
        total_sum += val
        max_val = max(max_val, val)

    target = total_sum // 2

    dp = [-1] * (target + 1)

    dp[0] = 0

    for v in range(1, max_val + 1):
        if counts[v] > 0:
            for s in range(target + 1):
                if dp[s] >= 0:
                    dp[s] = counts[v]
                elif s >= v and dp[s - v] > 0:
                    dp[s] = dp[s - v] - 1

    for s in range(target, -1, -1):
        if dp[s] >= 0:
            return (total_sum - s) - s

    return total_sum

