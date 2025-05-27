import math

def solution(N):

    for i in range(int(math.sqrt(N)), 0, -1):
        if N % i == 0:
            return ((N / i) + i) * 2
