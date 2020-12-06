import resource
import sys
from random import randint

# sys.setrecursionlimit(3929)
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)


# condicoes do problema
#     visitou[M[i,j]] = true
#     X--                      M[i,j] = 0
#     Y--                      M[i,j] < 0
#     0                        X=0 ou Y=0 ou visitou[M[i, j]] = true

# dificuldade: montagem dos casos!
# algoritmo de calcular todos os caminhos:
# cam(i, j, X, Y) = {
#     1                        i=0 e j=0
#     cam(i , j-1)             j>0 e i=0
#     cam(i, j+1)              j   e i=0
#     cam(i-1, j)              i> 0 e j=0
#     min( 1 + cam(i, j-1) + cam(i, j+1) + cam(i-1, j)) i>0 e j>0
# }
# como recuperar a soluçao?

def shortest_path(i, j, x, y):
    if memo[i][j] == -1:
        ans = 0
        if m[i][j] == 0:
            x -= x
        elif m[i][j] < 0:
            y -= y
        # if x < 0 or y < 0 or visited[i][j]:
        #     return ans
        # visited[i][j] = True

        if i == 0 and j == 0:               # base
            ans = 0
        elif 0 < j < M - 1 and i > 0:                      # esq, dir e cima
            ans = min(1 + shortest_path(i, j - 1, x, y), 1 + shortest_path(i, j + 1, x, y),
                      1 + shortest_path(i - 1, j, x, y))
        elif i > 0:
            if j > 0 and j == M - 1:                       # esq, cima
                ans = min(1 + shortest_path(i, j - 1, x, y), 1 + shortest_path(i - 1, j, x, y))
            elif j < M - 1 and j == 0:                     # dir, cima
                ans = min(1 + shortest_path(i, j + 1, x, y), 1 + shortest_path(i - 1, j, x, y))
            elif j == 0 and j == M - 1:                     # cima
                ans = 1 + shortest_path(i - 1, j, x, y)
        else:
            if 0 < j < M - 1:               # esq, dir
                ans = min(1 + shortest_path(i, j + 1, x, y), 1 + shortest_path(i, j - 1, x, y))
            elif j == M - 1:                # esq
                ans = 1 + shortest_path(i, j - 1, x, y)
        memo[i][j] = ans

    return memo[i][j]

# def print_path(i, w):
#     if i > 0 and w > 0:
#         if memo[i, w] == memo[i - 1][w]:
#             print_path(i - 1, w)
#         else:
#             print_path(i-1, w-)
#             print(i)


# N, M, X, Y = int(input("Digite N:")), int(input("Digite M: ")), int(input("Digite X: ")), int(input("Digite Y: "))
N, M, X, Y = 3, 2, 1, 1
m = []
visited = []
memo = []
for k in range(0, N):
    line = []
    flag = []
    lineOfMemo = []
    for p in range(0, M):
        line.append(randint(1, 9))
        flag.append(False)
        lineOfMemo.append(-1)
    m.append(line)
    visited.append(flag)
    memo.append(lineOfMemo)

print(sys.setrecursionlimit())
print("Resultado: ", shortest_path(N - 1, M - 1, X, Y))
print("Memo: ", memo)
