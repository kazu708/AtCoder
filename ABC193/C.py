import math

N = int(input())
ans = set()

for i in range(2,int(math.sqrt(N))+1):
    x = i*i
    while x <=N:
        ans.add(x)
        x *= i
print(N-len(ans))