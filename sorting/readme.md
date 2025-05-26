# 선택 정렬 - O(N^2)
최솟값을 찾아서 배열의 첫 번째 요소와 교환
```python
def selectionSort(A):
    n = len(A)
    for k in range(n):
        min_idx = k
        for j in range(k + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[k], A[min_idx] = A[min_idx], A[k]
    return A
```

# 계수 정렬 - O(N + K)
데이터를 정수 범위로 매핑하기
배열에 인덱스 순서대로 카운터 배열을 만든다.
이후에 인덱스 순서대로 카운터 배열에서 꺼내면 정렬 완료.
K개의 범위만큼 배열을 만들고 배열에서 꺼낸다. 0(2K) -> O(K)
N개의 요소만큼 카운트를 한다. O(N) -> O(N)
결국 O(N + K)


# 병합 정렬 - O(N logN)
정렬되지 않은 배열을 1개의 요소가 될 때까지 반으로 나눈다. 이후 정렬하면서 병합한다.
배열을 전체 반으로 나누는데 log2 N이 걸린다. 보기 좋게 log2 N을 logN이라 한다.
각 레벨별로 N만큼의 정렬 시간이 든다. 결국 N * logN의 시간이 든다.


각 언어의 내장 정렬함수들은 NlogN이다.


# 라인스위핑
보이지 않는 선을 왼쪽에서 오른쪽으로 쭉 밀면서 상황을 처리하는 알고리즘
