"""
bit全探索
"""

S = input()
N = len(S) - 1
ans = 0

for i in range(2**N):
    f = S[0]
    for v in range(N):
        if ((i >> v)&1):
            f += '+'
        f += S[v+1]

    ans += eval(f)

print(ans)