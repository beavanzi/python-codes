from random import randint

#condicoes do problema
#     visitou[M[i,j]] = true
#     X--                      M[i,j] = 0
#     Y--                      M[i,j] < 0
#     0                        X=0 ou Y=0 ou visitou[M[i, j]] = true

# dificuldade: montagem dos casos!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# cam(i, j, X, Y) = {
#     1                        i=0 e j=0
#     cam(i , j-1)             j>0 e i=0
#     cam(i, j+1)              j   e i=0
#     cam(i-1, j)              i> 0 e j=0
#     min( 1 + cam(i, j-1) + cam(i, j+1) + cam(i-1, j)) i>0 e j>0
# }

def shortestPath(i, j, x, y):
    if memo[i][j] == -1:
        if m[i][j] == 0:
            x -= x
        elif m[i][j] < 0:
            y -= y
        if x < 0 or y < 0 or visited[i][j]:
            return 0

        visited[i][j] = True

        if i == 0 and j == 0:
            ans = 0
        elif 0 < j < M-1 and i > 0:
            ans = min(1 + shortestPath(i, j - 1, x, y), 1 + shortestPath(i, j + 1, x, y), 1 + shortestPath(i - 1, j, x, y))
        elif j > 0 and i == 0:
            ans = 1 + shortestPath(i, j - 1, x, y)
        elif j < M-1 and i == 0:
            ans = 1 + shortestPath(i, j + 1, x, y)
        elif i > 0 and j == 0:
            ans = 1 + shortestPath(i - 1, j, x, y)
        memo[i][j] = ans

    return memo[i][j]


N = int(input("Digite N:"))
M = int(input("Digite M: "))
X = int(input("Digite X: "))
Y = int(input("Digite Y: "))
m = []
visited = []
memo = []

for i in range(0, N-1):
    line = []
    flag = []
    lineOfMemo = []
    for j in range(0, M-1):
        line.append(randint(1, 9))
        flag.append(False)
        lineOfMemo.append(-1)
    m.append(line)
    visited.append(flag)
    memo.append(lineOfMemo)

print(shortestPath(N - 1, M - 1, X, Y))














