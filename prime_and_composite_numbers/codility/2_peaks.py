def solution(A):
    N = len(A)
    if N < 3:
        return 0
    peaks = []
    for i in range(1, N - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)
    if len(peaks) <= 1:
        return len(peaks)

    def can_be_divided_by_blocks(k):
        length = N // k
        start = 0
        for peak in peaks:
            if start <= peak < start + length:
                start = start + length
        return start == N

    for i in range(len(peaks), 0, -1):
        if N % i == 0 and can_be_divided_by_blocks(i):
            return i

    return 1
