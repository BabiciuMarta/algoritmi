def inlocuire():
    sir = input()
    for caracter in sir:
        if caracter in 'aeiou':
            print(caracter.upper(), end="")
        else:
            print(caracter, end="")


def literamare():
    sir = input()
    sirnou = ""
    s = 0
    for caracter in sir:
        if s == 0:
            sirnou = sirnou + caracter.upper()
            print(caracter, "e primul")
        else:
            if s == (len(sir)-1):
                sirnou = sirnou + caracter.upper()
                print(caracter, "e ultimul")
            else:
                sirnou = sirnou + caracter
                print(caracter)
        s = s+1
        print(sirnou)


def halfsort():
    lista = [0, 2, 4, 45, 56, 3, 1, 30]
    jumatate = len(lista)//2
    primajumatate = lista[:jumatate:]
    primajumatate = primajumatate.sort()
    print(primajumatate)
    adouajumatate = lista[jumatate::]
    adouajumatate = adouajumatate.sort()
    print(adouajumatate)


if __name__ == "__main__":
    halfsort()
    inlocuire()
    literamare()
