def solution(S):
    stack = []
    for element in S:
        if element == "(":
            stack.append(element)
        else:
            if stack:
                stack.pop()
            else:
                return 0
    return 0 if stack else 1