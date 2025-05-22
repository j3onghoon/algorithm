"""
DP
Dynamic Programming

복잡한 문제를 더 작고 간단한 하위 문제로 나누어 해결하는 알고리즘.
각 하위 문제의 결과를 저장(메모이제이션)하여 같은 계산을 반복하지 않음으로써 효율성을 높인다.

핵심 특징
1. 중복되는 하위 문제들의 결과를 저장해두고 재활용
2. 최적 부분 구조: 큰 문제의 최적해가 작은 문제들의 최적해로 구성됨.
"""

def solution(numbers, target):
    dp = {0: 1}

    for num in numbers:
        next_dp = {}
        for current_sum, count in dp.items():
            next_dp[current_sum + num] = next_dp.get(current_sum + num, 0) + count
            next_dp[current_sum - num] = next_dp.get(current_sum - num, 0) + count
        dp = next_dp
    return dp.get(target, 0)
