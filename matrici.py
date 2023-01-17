def matrice_patratica1():
    matrice = []
    coloane = 4
    rand = 4
    for i in range(4):
        for j in range(4):
            matrice[i][j] = int(input())
            if i < j:
                s1 = coloane + matrice[i][j]
            if i + j < 4:
                s2 = rand + matrice[i][j]


def suma_matrice():
    n = 4
    matrice = [[0] * n for _ in range(n)]
    sdp = 0
    sds = 0

    for i in range(n):
        for j in range(n):
            print(i, ",", j, end="=")
            matrice[i][j] = int(input())
            if i < j:
                sdp = sdp + matrice[i][j]
            if i + j < n-1:
                sds = sds + matrice[i][j]
    print("")
    print("suma diag.princ. = ", sdp)
    print("suma diag. sec. = ", sds)


def patrat_matrice():
    n = 4
    matrice = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            print(i, ",", j, end="=")
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j]**2
    print("")
    for i in range(n):
        for j in range(n):
            print(matrice[i][j], end=",")
        print("")


def cifra2_matrice():
    n = 4
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            print(i, ",", j, end="=")
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j]+2
    print("")
    for i in range(n):
        for j in range(n):
            print(matrice[i][j], end=",")
        print("")


if __name__ == "__main__":
    suma_matrice()
    patrat_matrice()
    cifra2_matrice()

