import numpy as np

n, m = map(int, input().split())
array = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.mean(array, axis=1))
print(np.var(array, axis=0))
print(np.std(array))






