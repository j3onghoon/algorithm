def solution(A):
    N = len(A)
    prefix_sum = [0] * (N + 1)

    for i, val in enumerate(A):
        prefix_sum[i + 1] = prefix_sum[i] + val

    before_min_avg = float('inf')
    min_avg = before_min_avg
    min_index = 0
    for i in range(N - 1):
        min_avg = min(min_avg, (prefix_sum[i + 2] - prefix_sum[i]) / 2)
        if before_min_avg != min_avg:
            before_min_avg = min_avg
            min_index = i
        if i < N - 2:
            min_avg = min(min_avg, (prefix_sum[i + 3] - prefix_sum[i]) / 3)
            if before_min_avg != min_avg:
                before_min_avg = min_avg
                min_index = i

    return min_index