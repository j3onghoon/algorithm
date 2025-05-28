def solution(N, M):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return N // gcd(N, M)
