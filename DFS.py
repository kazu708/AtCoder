'''
深さ優先探索
'''

import sys
sys.setrecursionlimit(100000000)

H , W = map(int,input().split(' '))

M = [list(input()) for _ in range(H)]

for i in range(H):
    for v in range(W):
        if M[i][v] == 's':
            sx , sy = i ,v
        if M[i][v] == 'g':
            gx , gy = i ,v

visited = [[False] * W for i in range(H)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    visited[x][y] = True
    for x2, y2 in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
        if (0 <= x2 < H and 0 <= y2 < W ) and not (M[x2][y2] == '#'):
            if not visited[x2][y2]:
                dfs(x2, y2)

dfs(sx,sy)
if visited[gx][gy]:
    print('Yes')
else:
    print('No')




