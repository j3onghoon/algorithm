def solution(N, P, Q):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False

    primes = [i for i in range(2, N + 1) if is_prime[i]]

    is_semiprime = [False] * (N + 1)

    for i in range(len(primes)):
        for j in range(i, len(primes)):
            semiprime = primes[i] * primes[j]
            if semiprime > N:
                break
            is_semiprime[semiprime] = True

    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (1 if is_semiprime[i] else 0)

    result = []
    for p, q in zip(P, Q):
        count = prefix_sum[q] - prefix_sum[p - 1]
        result.append(count)

    return result
