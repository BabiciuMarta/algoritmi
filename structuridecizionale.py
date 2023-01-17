# de realizat o functie care preia un numar de la tastatura  si incadreaza acel numar in domeniile urmatoare:
# 0 -> 3500  - mic
# 3500 -> 7000 - mediu
# 7000 ->   - mare

# tema ex nolis base decizionalarepetitiva

def sir5():
    print("introduceti un sir de numere naturale:")
    sir = input()
    contor = 0
    for index in range(0, len(sir)):
        if int(sir[index]) == 5:
            contor += 1
    print("contor=", contor)


def lista5():
    print("introduceti un sir de numere naturale despartite prin spatiu:")
    lista = input().split(" ")
    print(lista)
    contor = 0
    for index in range(0, len(lista)):
        if int(lista[index]) == 5:
            contor += 1
    print("contor=", contor)


def adunare():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a+b=", a+b)


def scadere():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a-b=", a-b)


def inmultire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a*b=", a*b)


def impartire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a/b=", a/b)


def incadrare():
    print(" introduceti un numar:", end="")
    nr = int(input())
    if nr < 3500:
        print("mic")
    else:
        if nr < 7000:
            print("mediu")
        else:
            print("mare")


def meniu():
    print("Apasati tasta 1 pentru adunare, 2 pentru scadere, 3 pentru inmultire, 4 pentru impartire")
    o = input().strip()
    if o == "1":
        print("adunare")
        adunare()

    else:
        if o == "2":
            print("scadere")
            scadere()
        else:
            if o == "3":
                print("inmultirea")
                inmultire()
            else:
                if o == "4":
                    print("impartire")
                    impartire()
                else:
                    print("tastati doar 1, 2, 3, 4")


if __name__ == "__main__":
    lista5()
    incadrare()
    sir5()
