S = str(input())
flag1 = True
flag2 = True

for i in range(len(S)):
    char = S[i]
    if (i+1) % 2 == 0:
        if char.isupper():
            flag1 = True
        else:
            flag1 = False
            break
    if (i+1) %2 != 0:
        if char.islower():
            flag2 = True
        else:
            flag2 = False
            break

if flag1 == True and flag2==True :
    print('Yes')
else:
    print('No')

