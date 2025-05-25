# nonlocal
# 중첩 함수에서 외부 함수의 변수를 수정할 때 사용.
# 가장 가까운 외부 함수 범위에서 변수를 찾는다.
# 전역 범위의 변수에는 사용할 수 없다.
# global
# 함수에서 전역 변수를 수정할 때 사용
# 항상 모듈 레벨의 전역 범위에서 변수를 찾는다.
#
# 단순연산 - 5회 이상 반복 연산하는 경우 저장하는 게 유리


def solution(numbers, target):
    answer = 0

    N = len(numbers)
    def dfs(idx, current_sum):
        nonlocal answer

        if idx == N and current_sum == target:
            answer += 1
        if idx < N:
            dfs(idx + 1, current_sum + numbers[idx])
            dfs(idx + 1, current_sum - numbers[idx])

    dfs(0, 0)
    return answer



















"""
# 복잡한 연산 - 2회 이상 반복 연산하는 경우 저장하는 게 유리

def solution(numbers, target):
    count = 0

    N = len(numbers)
    def dfs(idx, current_sum):
        nonlocal count

        if idx == N:
            if current_sum == target:
                count += 1
            return

        dfs(idx + 1, current_sum + numbers[idx])
        dfs(idx + 1, current_sum - numbers[idx])

    dfs(0, 0)
    return count

"""