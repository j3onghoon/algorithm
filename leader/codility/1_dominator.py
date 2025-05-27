def solution(A):
    N = len(A)
    if N == 0:
        return -1

    candidate = A[0]
    count = 1
    candidate_index = 0

    for i in range(1, N):
        if A[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = A[i]
                candidate_index = i
                count = 1

    actual_count = A.count(candidate)
    if actual_count > len(A) // 2:
        return candidate_index
    return -1

