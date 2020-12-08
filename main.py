import sys
from random import randint

sys.setrecursionlimit(100000)


def lowest_cost(i, j, x, y, pos):
    if memo[i][j] == -10000:
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
                    ans = min(m[i][j] + lowest_cost(i, j + 1, x, y, "e"),
                              m[i][j] + lowest_cost(i - 1, j, x, y, "c"))
                else:                                    # cima
                    ans = int(m[i][j] + lowest_cost(i - 1, j, x, y, "c"))
        elif pos == "d":
            if i > 0:
                if 0 < j <= M - 1:                             # esq, cima
                    ans = min(m[i][j] + lowest_cost(i, j - 1, x, y, "d"),
                              m[i][j] + lowest_cost(i - 1, j, x, y, "c"))
                else:                                           # cima
                    ans = int(m[i][j] + lowest_cost(i - 1, j, x, y, "c"))
            elif i == 0:
                if j > 0:  # esq
                    ans = int(m[i][j] + lowest_cost(i, j - 1, x, y, "d"))
        else:
            if 0 < j < M - 1 and i > 0:                     # esq, dir e cima
                ans = min(m[i][j] + lowest_cost(i, j - 1, x, y, "d"), m[i][j] + lowest_cost(
                    i, j + 1, x, y, "e"),  m[i][j] + lowest_cost(i - 1, j, x, y, "c"))
            elif i > 0:
                if 0 < j <= M - 1:                       # esq, cima
                    ans = min(m[i][j] + lowest_cost(i, j - 1, x, y, "d"),
                              m[i][j] + lowest_cost(i - 1, j, x, y, "c"))
                elif 0 <= j < M - 1:                     # dir, cima
                    ans = min(m[i][j] + lowest_cost(i, j + 1, x, y, "e"),
                              m[i][j] + lowest_cost(i - 1, j, x, y, "c"))
                else:                                   # cima
                    ans = int(m[i][j] + lowest_cost(i - 1, j, x, y, "c"))
            elif i == 0:
                if j > 0:                                       # esq
                    ans = int(m[i][j] + lowest_cost(i, j - 1, x, y, "d"))

        memo[i][j] = ans

    return memo[i][j]


# Função de recuperação da solução ótima
def print_path(i, w, pos):
    if i == 0 and w == 0:
        print(m[i][w])
    elif pos == "e":
        if i > 0:
            if 0 <= w < M - 1:      # dir, cima
                if memo[i][w] >= 0:
                    if int(memo[i][w]) >= abs(memo[i][w + 1]):
                        print_path(i, w + 1, "e")
                        print(m[i][w])

                    elif int(memo[i][w]) >= abs(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])

                else:
                    if int(memo[i][w]) >= int(memo[i][w + 1]):
                        print_path(i, w + 1, "e")
                        print(m[i][w])

                    elif int(memo[i][w]) >= int(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])
            else:
                if memo[i][w] >= 0:
                    if int(memo[i][w]) >= abs(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])

                else:
                    if int(memo[i][w]) >= int(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])
    elif pos == "d":
        if i > 0:
            if 0 < w <= M - 1:
                if memo[i][w] >= 0:
                    if int(memo[i][w]) >= abs(memo[i][w - 1]):
                        print_path(i, w - 1, "d")
                        print(m[i][w])

                    elif int(memo[i][w]) >= abs(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])
                else:
                    if int(memo[i][w]) >= int(memo[i][w - 1]):
                        print_path(i, w - 1, "d")
                        print(m[i][w])

                    elif int(memo[i][w]) >= int(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])
            else:
                if memo[i][w] >= 0:
                    if int(memo[i][w]) >= abs(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])
                else:
                    if int(memo[i][w]) >= int(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])

        elif i == 0:
            if w > 0:
                if memo[i][w] >= 0:
                    if int(memo[i][w]) >= abs(memo[i][w - 1]):
                        print_path(i, w - 1, "d")
                        print(m[i][w])
                else:
                    if int(memo[i][w]) >= int(memo[i][w - 1]):
                        print_path(i, w - 1, "d")
                        print(m[i][w])
    else:
        if 0 < w < M - 1 and i > 0:                     # esq, dir e cima
            if memo[i][w] >= 0:
                if int(memo[i][w]) >= abs(memo[i - 1][w]):
                    print_path(i - 1, w, "c")
                    print(m[i][w])

                elif int(memo[i][w]) >= abs(memo[i][w + 1]):
                    print_path(i, w + 1, "e")
                    print(m[i][w])

                elif int(memo[i][w]) >= abs(memo[i][w - 1]):
                    print_path(i, w - 1, "d")
                    print(m[i][w])
            else:
                if int(memo[i][w]) >= int(memo[i - 1][w]):
                    print_path(i - 1, w, "c")
                    print(m[i][w])

                elif int(memo[i][w]) >= int(memo[i][w + 1]):
                    print_path(i, w + 1, "e")
                    print(m[i][w])

                elif int(memo[i][w]) >= int(memo[i][w - 1]):
                    print_path(i, w - 1, "d")
                    print(m[i][w])
        elif i > 0:
            if 0 < w <= M - 1:                       # esq, cima
                if memo[i][w] >= 0:
                    if int(memo[i][w]) >= abs(memo[i][w - 1]):
                        print_path(i, w - 1, "d")
                        print(m[i][w])

                    elif int(memo[i][w]) >= abs(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])

                else:
                    if int(memo[i][w]) >= int(memo[i][w - 1]):
                        print_path(i, w - 1, "d")
                        print(m[i][w])

                    elif int(memo[i][w]) >= int(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])
            elif 0 <= w < M - 1:                     # dir, cima
                if memo[i][w] >= 0:
                    if int(memo[i][w]) >= abs(memo[i][w + 1]):
                        print_path(i, w + 1, "e")
                        print(m[i][w])

                    elif int(memo[i][w]) >= abs(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])

                else:
                    if int(memo[i][w]) >= int(memo[i][w + 1]):
                        print_path(i, w + 1, "e")
                        print(m[i][w])

                    elif int(memo[i][w]) >= int(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])
            else:                                   # cima
                if memo[i][w] >= 0:
                    if int(memo[i][w]) >= abs(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])

                else:
                    if int(memo[i][w]) >= int(memo[i - 1][w]):
                        print_path(i - 1, w, "c")
                        print(m[i][w])
        elif i == 0:
            if w > 0:                                       # esq
                if memo[i][w] >= 0:
                    if int(memo[i][w]) >= abs(memo[i][w - 1]):
                        print_path(i, w + 1, "d")
                        print(m[i][w])
                else:
                    if int(memo[i][w]) >= int(memo[i][w - 1]):
                        print_path(i, w + 1, "d")
                        print(m[i][w])

# estas duas linhas a baixo foram criadas para que digitemos N, M, X, Y, mas vamos considerar entradas de teste para facilitar
# N, M, X, Y = int(input("Digite N:")), int(input("Digite M: ")), int(input("Digite X: ")), int(input("Digite Y: "))
# m = []


# TESTE 1
N, M, X, Y = 9, 5, 1, 1
m = [[8, 4, 8, 3, 1], [1, 4, 7, 7, 8], [1, 2, 6, 4, 7], [1, 1, 2, 3, 8], [
    1, 3, 9, 5, 7], [1, 1, 1, 5, 8], [1, 9, 7, 6, 6], [1, 5, 3, 9, 8], [1, 1, 1, 1, 1]]

# TESTE 2
#N, M, X, Y = 2, 2, 1, 1
# m = [[4, 3], [1, 7]]

# TESTE 3
#N, M, X, Y = 2, 4, 2, 1
# m = [[3, 3, 2, 1], [1, 9, 10, 1], [1, 1, 1, 5]]

# TESTE 4
#N, M, X, Y = 2, 5, 1, 9
# m = [[2, 0, 0, 3, 0], [1, 4, 7, 0, 8]]

# TESTE 5
#N, M, X, Y = 2, 5, 1, 0
# m = [[2, 0, 0, 3, -1], [1, 4, 7, -1, 8]]

memo = []
# o line servia pra criarmos matrizes com preenchimento aleatorio
for k in range(N):
    # line = []
    lineOfMemo = []
    for p in range(M):
        # line.append(randint(-30, 30))
        lineOfMemo.append(-10000)
    # m.append(line)
    memo.append(lineOfMemo)

result = lowest_cost(N - 1, M - 1, X, Y, "n")
print('Impossivel.') if result >= 100000 else print("Resultado: ", result)
if result >= 100000:
    print('Sem caminho recuperável.')
else:
    print("Melhor caminho: (começa a printar a partir do 0,0 e vai até N-1,M-1)")
    print_path(N-1, M-1, "n")

print("\n\nMatriz: ", m)
print("Memo: ", memo)
