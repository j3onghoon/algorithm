def solution(A):
    west = 0
    answer = 0
    for car in reversed(A):
        if car == 1:
            west += 1
        elif car == 0:
            answer += west
            if answer > 1_000_000_000:
                return -1

    return answer
