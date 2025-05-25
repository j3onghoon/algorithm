# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A: list):
    positive_set = {element for element in A if element > 0}
    expected_set = set(range(1, len(A) + 2))

    return min(expected_set - positive_set)
