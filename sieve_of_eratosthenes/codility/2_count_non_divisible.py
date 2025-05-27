def solution(A):
    N = len(A)
    if N == 0:
        return []

    max_val = max(A)
    count = [0] * (max_val + 1)
    for num in A:
        count[num] += 1

    divisor_count = [0] * (max_val + 1)

    for i in range(1, max_val + 1):
        if count[i] > 0:
            for multiple in range(i, max_val + 1, i):
                divisor_count[multiple] += count[i]

    result = []
    for num in A:
        non_divisors = N - divisor_count[num]
        result.append(non_divisors)

    return result
