A = set(input().split())
n = int(input())
result = all(A > set(input().split()) for _ in range(n))
print(result)
