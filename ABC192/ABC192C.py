N , K = map(str,input().split(' '))

for i in range(int(K)):
    fa = list(N)

    fa_acs = sorted(fa,reverse=False)
    fa_desc = sorted(fa,reverse=True)

    num_acs = ''.join(fa_acs)
    num_desc = ''.join(fa_desc)

    acs = int(num_acs)
    decs = int(num_desc)

    N = decs - acs
    N = str(N)
print(N)