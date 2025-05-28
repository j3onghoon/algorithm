def go_up_ladder(n):
    result = [0, 1, 2]

    while len(result) < n + 1:
        result.append(result[-1] + result[-2])

    return result

def solution(A, B):
    ladder_counts = [0, 1, 2]
    max_ladder = max(A)
    divisor = 2 ** max(B)
    while len(ladder_counts) < max_ladder + 1:
        ladder_counts.append((ladder_counts[-1] + ladder_counts[-2]) % divisor)

    return [ladder_counts[a] % (2 ** b) for a, b in zip(A, B)]
