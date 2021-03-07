'''
Greedy
文字を反転させ後ろから一致するか判定する
'''

S = input()

#入力文字の反転
S_rev = S[::-1]
divide = ['dream','dreamer','erase','eraser']
divide_rev = []

#すべて反転可能ならflagをTrueに変更する
flag = False

#分割する文字の反転
for i in divide:
    temp = i[::-1]
    divide_rev.append(temp)

for v in range(len(S_rev)):
    for words in divide_rev:
        if S_rev[:len(words)] == words:
            S_rev = S_rev[len(words)::]
            if len(S_rev) == 0:
                flag = True
                break

if flag == True:
    print('YES')
else:
    print('NO')