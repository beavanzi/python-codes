import sys
from random import randint

sys.setrecursionlimit(100000)

# condicoes do problema
#     X--                      M[i,j] = 0
#     Y--                      M[i,j] < 0
#     0                        X < 0 ou Y < 0

# algoritmo de calcular todos os caminhos:
# cam(i, j, X, Y) = {
#     1                        i=0 e j=0
#     cam(i , j-1)             j>0 e i=0
#     cam(i, j+1)              j   e i=0
#     cam(i-1, j)              i> 0 e j=0
#     min( 1 + cam(i, j-1) + cam(i, j+1) + cam(i-1, j)) i>0 e j>0
# }
# como recuperar a soluçao?


def shortest_path(i, j, x, y, pos):
    if memo[i][j] == -1:
        ans = 0
        if m[i][j] == 0:
            x = x - 1
        elif m[i][j] < 0:
            y = y - 1
        if x < 0 or y < 0:
            return 100000000
        if i == 0 and j == 0:                                   # base
            ans = m[i][j]
        elif pos == "e":
            if i > 0:
                if 0 <= j < M - 1:                        # dir, cima
                    ans = min(m[i][j] + shortest_path(i, j + 1, x, y, "e"),
                              m[i][j] + shortest_path(i - 1, j, x, y, "c"))
                else:                                    # cima
                    ans = int(m[i][j] + shortest_path(i - 1, j, x, y, "c"))
        elif pos == "d":
            if i > 0:
                if 0 < j <= M - 1:                             # esq, cima
                    ans = min(m[i][j] + shortest_path(i, j - 1, x, y, "d"),
                              m[i][j] + shortest_path(i - 1, j, x, y, "c"))
                else:                                           # cima
                    ans = int(m[i][j] + shortest_path(i - 1, j, x, y, "c"))
            elif i == 0:
                if j > 0:  # esq
                    ans = int(m[i][j] + shortest_path(i, j - 1, x, y, "d"))
        else:
            if 0 < j < M - 1 and i > 0:                     # esq, dir e cima
                ans = min(m[i][j] + shortest_path(i, j - 1, x, y, "d"), m[i][j] + shortest_path(
                    i, j + 1, x, y, "e"),  m[i][j] + shortest_path(i - 1, j, x, y, "c"))
            elif i > 0:
                if 0 < j <= M - 1:                       # esq, cima
                    ans = min(m[i][j] + shortest_path(i, j - 1, x, y, "d"),
                              m[i][j] + shortest_path(i - 1, j, x, y, "c"))
                elif 0 <= j < M - 1:                     # dir, cima
                    ans = min(m[i][j] + shortest_path(i, j + 1, x, y, "e"),
                              m[i][j] + shortest_path(i - 1, j, x, y, "c"))
                else:                                   # cima
                    ans = int(m[i][j] + shortest_path(i - 1, j, x, y, "c"))
            elif i == 0:
                if j > 0:                                       # esq
                    ans = int(m[i][j] + shortest_path(i, j - 1, x, y, "d"))

        memo[i][j] = ans

    return memo[i][j]


def print_path(i, w):
    if i > 0:
        if 0 < w < M-1:
            if int(memo[i][w]) > int(memo[i - 1][w]):
                print_path(i - 1, w)
                print(m[i][w])

 #           elif int(memo[i][w]) == int(memo[i - 1][w + 1]):
 #               print_path(i - 1, w + 1)
 #               print(m[i][w])

 #           elif int(memo[i][w]) == int(memo[i - 1][w - 1]):
 #               print_path(i - 1, w - 1)
 #               print(m[i][w])
            elif int(memo[i][w]) > int(memo[i][w + 1]):
                print_path(i, w + 1)
                print(m[i][w])

            elif int(memo[i][w]) > int(memo[i][w - 1]):
                print_path(i, w - 1)
                print(m[i][w])

        elif 0 < w <= M - 1:
            if int(memo[i][w]) > int(memo[i][w - 1]):
                print_path(i, w - 1)
                print(m[i][w])

            elif int(memo[i][w]) > int(memo[i - 1][w]):
                print_path(i - 1, w)
                print(m[i][w])

        elif 0 <= w < M - 1:
            if int(memo[i][w]) > int(memo[i][w + 1]):
                print_path(i, w + 1)
                print(m[i][w])

            elif int(memo[i][w]) > int(memo[i - 1][w]):
                print_path(i - 1, w)
                print(m[i][w])

#           elif int(memo[i][w]) == int(memo[i - 1][w - 1]):
#                print_path(i - 1, w - 1)
#                print(m[i][w])

        # else:
        #         print_path(i - 1, w - 1)
        #         print(m[i][w])

    elif i == 0:
        if 0 < w <= M-1:
            if int(memo[i][w]) == int(memo[i][w - 1]):
                print_path(i, w - 1)
                print(m[i][w])

        #     elif int(memo[i][w]) == int(memo[i][w + 1]):
        #         print_path(i, w - 1)
        #         print(m[i][w])

        #     else:
        #         print_path(i, w - 1)
        #         print(m[i][w])

        # elif 0 < w <= M - 1:
        #     if int(memo[i][w]) == int(memo[i][w - 1]):
        #         print_path(i, w - 1)
        #         print(m[i][w])


# N, M, X, Y = int(input("Digite N:")), int(input("Digite M: ")), int(input("Digite X: ")), int(input("Digite Y: "))
N, M, X, Y = 2, 5, 1, 1
#m = []
#m = [[4, 3], [1, 7]]
# m = [[3, 3, 2, 1], [1, 9, 10, 1], [1, 1, 1, 5]]
m = [[2, 0, 0, 3, 0], [1, 4, 7, 0, 8]]
# m = [[2, 0, 0, 3, -1], [1, 4, 7, -1, 8]]
# m = [[8, 4, 8, 3, 1], [1, 4, 7, 7, 8], [1, 2, 6, 4, 7], [1, 1, 2, 3, 8], [1, 3, 9, 5, 7], [1, 1, 1, 5, 8], [1, 9, 7, 6, 6], [1, 5, 3, 9, 8], [1, 1, 1, 1, 1]]
visited = []
memo = []
for k in range(N):
    # line = []
    flag = []
    lineOfMemo = []
    for p in range(M):
        # line.append(randint(1, 9))
        flag.append(False)
        lineOfMemo.append(-1)
    # m.append(line)
    visited.append(flag)
    memo.append(lineOfMemo)

result = shortest_path(N - 1, M - 1, X, Y, "n")
print('Impossivel.') if result >= 100000 else print("Resultado: ", result)
print('Sem caminho recuperável.') if result >= 100000 else print(
    "Melhor caminho: ", print_path(N-1, M-1))
print("Matriz: ", m)
print("Memo: ", memo)
