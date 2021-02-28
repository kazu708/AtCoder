N = int(input())


Store = [list(map(int,input().split())) for i in range(N)]
Costs = []

for i in range(N):
    if Store[i][0] < Store[i][2]:
        temp = Store[i][1]
        Costs.append(temp)

if len(Costs) != 0:
    print(min(Costs))
else:
    print(-1)



