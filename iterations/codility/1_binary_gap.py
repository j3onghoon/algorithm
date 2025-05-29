def solution(N):
    target = bin(N)[2:].rstrip("0")

    candidates = target.split("1")

    max_length = 0
    for zeros in candidates:
        max_length = max(max_length, len(zeros))

    return max_length
