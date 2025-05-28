def solution(A, B, C):
    m = len(C)
    beg = 0
    end = m

    result = -1
    while end >= beg:
        mid = (beg+end)/2
        if check(A, B, C, mid):
            end = mid - 1
            result = mid
        else:
            beg = mid+1

    return result


def check(A, B, C, candidate):
    nails = [0] * 2 * (len(C) + 1)

    for index in range(0, candidate):
        nails[C[index]] += 1

    for index in range(1, len(nails)):
        nails[index] += nails[index-1]

    for index in range(len(A)):
        if (nails[B[index]] - nails[A[index]-1]) == 0:
            return False

    return True