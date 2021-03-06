N , Y = map(int,input().split(' '))

flag = False

for k in range(N+1):
    for l in range(N+1):
        n = N - k -l
        if n >= 0:
            sum = 10000*k + 5000*l + 1000*n
            if sum == Y:
                flag = True
                print(k,l,n)
                quit()

if flag == False:
    print(-1,-1,-1)