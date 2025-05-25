def solution(N, A):
    result = [0] * N
    max_value = 0
    current_max = 0

    for element in A:
        if element == N + 1:
            max_value = current_max
        else:
            if result[element - 1] < max_value:
                result[element - 1] = max_value

            result[element - 1] += 1
            current_max = max(current_max, result[element - 1])

    for i in range(N):
        if result[i] < max_value:
            result[i] = max_value

    return result
