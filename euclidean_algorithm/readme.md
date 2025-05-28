# 유클리드 호제법
두 양의 정수의 최대 공약수를 계산하는 문제 해결

gcd(a, b) = gcd(b, r)
r = a mod b
a = b * t + r


```python
# O(log(min(a,b))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 오버플로우를 안하려고 //을 먼저 한다.
def lcm(a, b):
    return a // gcd(a, b) * b
```
