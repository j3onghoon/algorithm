def solution(A, B):
    stack = []
    """
    숫자가 낮을수록 상류
    0은 상류로 1은 하류로
    """
    count = 0
    for i in range(len(A)):
        if B[i] == 1:
            stack.append(i)
        else:
            while stack:
                down_fish = stack.pop()
                if A[down_fish] < A[i]:
                    continue
                else:
                    stack.append(down_fish)
                    break
            else:
                count += 1

    return count + len(stack)
