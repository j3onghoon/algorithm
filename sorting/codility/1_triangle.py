
def solution(A):
    A.sort()

    for i in range(len(A) - 1, 1, -1):
        if A[i - 2] <= 0:
            break
        if A[i] - A[i - 1] < A[i - 2]:
                return 1
    return 0


a + b > c
a + c > b
b + c > a