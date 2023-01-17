sm = 0


def adunarecametoda(*args):
    global sm
    for a in args:
        sm += a


def adunare(s=0, *a):
    for element in a:
        s = s + element
    return s


def adunare2lista(lista):
    listanoua = list()
    for i in range(len(lista)):
        listanoua.append(lista[i]+2)
    return listanoua


def inmultire2lista(lista):
    listanoua = list()
    for i in range(len(lista)):
        listanoua.append(lista[i]*2)
    return listanoua


def oglindit(n):
    return int(str(n)[::-1])

# primul parametru e o lista de nr intregi iar al 2 lea parametru reprezinta valoarea initiala


def adunarelista(lista, s=0):
    for i in range(len(lista)):
        s += lista[i]
    return s


# gasirea primului nr prim mai mae ca si n
def nr_prim(numar):
    # am nevoie de o variabila sa mi spuna ca am gasit nr prim
    # initializez variabila respectiva cu false sau 0
    gasit = 0
    # cat timp nu am gasit nr
    while gasit == 0:
        # maresc nr meu cu 1 si verific daca este prim
        numar = numar + 1
        # daca e prim modific variabila gasita in true, prin urmare while-ul se va opri
        if verificarePrime(numar):
            gasit = 1
    # reintorc nr gasit
    return numar


# opt poate lua valori 1, 2 sau 3, unde 1 - adunare, 2 - scadere, 3 - produs
def meniu3(opt):
    # specificam tipul parametrilor si ce reprezinta fiecare
    if opt == 1:
        return "adunare"
    elif opt == 2:
        return "scadere"
    elif opt == 3:
        return "inmultire"
    else:
        return "operatie nedefinita"


def verificarePrime(numar):
    # daca nr e 2 atunci e un prim
    if numar == 2:
        return True
    # daca e mai mic ca si 2 atunci nu este prim
    if numar < 2:
        return False
    # daca nr se imparte exact la 2 atunci nu e prim
    if numar % 2 == 0:
        return False
    # luam nr de la 3 pana la valoarea nr impartite la 2
    for divizor in range(3, numar // 2):
        # daca nr se imparte la divizor atunci nu e prim
        if numar % divizor == 0:
            return False
    # daca s a ajuns aici inseamna ca nr meu este prim
    return True


def cifrazero(n):
    # am convertit nr meu in sir de caractere
    sir = str(n)
    # am initializat un contor cu 0
    contor = 0
    # pentru fiecare caracter din sirul meu
    for caracter in sir:
        # verific daca e 0 iar daca da atunci incrementez contorul
        if caracter == "0":
            contor += 1
    # intorc ca si rezultat al functiei contorul dfinit de mine
    return contor


# produsul unor nr primite ca parametru de o functie
def produsul(*args):
    p = 1
    for a in args:
        p = p * a
    return p

# factorul unui nr n, n!


def factorial(n):
    f = 1
    i = 1
    # varianta cu while
    while i <= n:
        f = f * 1
        i = i+1
    # varianta cu for
    for i in range(1, n+1):
        f = f*i
    return f


if __name__ == "__main__":
    print(oglindit(123456))
    adunarecametoda(1, 2, 4, 5)
    print(sm)
    print(adunare(1, 2, 4, 5))
    print(adunare2lista([1, 2, 3, 4]))
