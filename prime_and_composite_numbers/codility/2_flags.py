def solution(A):
    n = len(A)

    if n < 3:
        return 0

    peaks = []
    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)

    if not peaks:
        return 0

    if len(peaks) == 1:
        return 1

    def can_place_k_flags(k):
        if k > len(peaks):
            return False

        placed = 1
        last_flag_pos = peaks[0]

        for peak in peaks[1:]:
            if peak - last_flag_pos >= k:
                placed += 1
                last_flag_pos = peak
                if placed == k:
                    return True

        return False

    left, right = 1, int(n ** 0.5) + 1
    result = 1

    while left <= right:
        mid = (left + right) // 2
        if can_place_k_flags(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result
