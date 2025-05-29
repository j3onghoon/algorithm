def solution(M, A):
    N = len(A)

    seen = [False] * (M + 1)

    left = 0
    count = 0

    for right in range(N):
        current_val = A[right]

        while seen[current_val]:
            seen[A[left]] = False
            left += 1

        seen[current_val] = True

        count += (right - left + 1)

        if count >= 1_000_000_000:
            return 1_000_000_000

    return count
