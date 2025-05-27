def solution(N):
    if N == 1:
        return 1
    i = 2
    count = 2

    while i * i <= N:
        if N % i == 0:
            if i * i == N:
                count += 1
            else:
                count += 2
        i += 1

    return count
