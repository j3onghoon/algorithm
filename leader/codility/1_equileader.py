def solution(A):
    N = len(A)
    if N <= 1:
        return 0

    candidate, leader_count = find_leader(A, N)
    if leader_count <= N // 2:
        return 0

    equi_leaders = 0
    left_count = 0

    for i in range(N - 1):
        if A[i] == candidate:
            left_count += 1

        left_size = i + 1
        right_size = N - i - 1
        right_count = leader_count - left_count

        if (left_count > left_size // 2 and
            right_count > right_size // 2):
            equi_leaders += 1

    return equi_leaders

def find_leader(A, N):
    candidate = A[0]
    count = 1

    for i in range(1, N):
        if A[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = A[i]
                count = 1

    return candidate, A.count(candidate)