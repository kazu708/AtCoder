"""
bit全探索
"""
S = list(input())

ans = 0
for i in range(2**3):
    func = S[0]

    for v in range(3):
        if ((i>>v))&1:
            func += '+'
        else:
            func += '-'
        func += S[v+1]

    ans = eval(func)
    if ans == 7:
        print(func + '=7')
        quit()

