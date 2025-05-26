OPEN_BRACKETS = ["{", "[", "("]
CLOSE_BRACKETS = ["}", "]", ")"]
BRACKETS = {CLOSE_BRACKETS[i]: OPEN_BRACKETS[i] for i in range(len(CLOSE_BRACKETS))}

def solution(S):
    stack = []

    for element in S:
        if element in OPEN_BRACKETS:
            stack.append(element)
        elif element in CLOSE_BRACKETS:
            if not stack:
                return 0
            last = stack.pop()
            if last != BRACKETS[element]:
                return 0

    return 1 if not stack else 0
