K , S = map(int,input().split(' '))

cnt = 0

for k in range(K+1):
    for l in range(K+1):
        n = S - l - k
        if n <= K and n >= 0:
            cnt += 1

print(cnt)