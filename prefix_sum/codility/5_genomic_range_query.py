def solution(S, P, Q):



    start_value = ord("A")
    result = []
    for i in range(len(P)):
        start = P[i]
        end = Q[i]
        min_value = ord(min(set(S[start:end + 1])))
        result.append(min_value - start_value)
    return result