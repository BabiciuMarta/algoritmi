def parcurgere_lista():
    l1 = list()
    l1 = [100, 10, 200, 23, 134, 50, 40]
    for element in l1:
        print(element)
    for i in range(len(l1)):
        print(l1[i])


# am cuvantul abc, iar a are valoarea 10, b 20, c 30 -> 10+20+30
# {a:10, b:20, c:30, ....}

def suma_litere():
    # definesc dictionarul/ hash table
    # sub forma de mai jos
    dic1 = {'a': 10, 'b': 20, 'c': 300}

    suma = 0
    cu = 'abc'
    for i in range(len(cu)):
        suma += dic1[cu[i]]
    print("suma este:", suma)


def cript_hash(propozitie):
    dict3crypt = {'a': 'd', 'b': 'e', 'c': 'f', 'd': "g", 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k',
                  'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r', 'p': 's',
                  'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a',
                  'y': 'b', 'z': 'c'}
    propozitie = input('introduceti o propozitie:')
    rezultat = ''
    for element in propozitie:
        if element in (' ', ',', '-', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            rezultat += element
        else:
            rezultat += dict3crypt[element]
    return rezultat


def decript_hash(propozitie):
    dict3decrypt = {'d': 'a', 'e': 'b', 'f': 'c', 'g': "d", 'h': 'e', 'i': 'f', 'j': 'g', 'k': 'h',
                  'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n', 'r': 'o', 's': 'p',
                  't': 'q', 'u': 'r', 'v': 's', 'w': 't', 'x': 'u', 'y': 'v', 'z': 'w', 'a': 'x',
                  'b': 'y', 'c': 'z'}
    rezultat = ''
    for element in propozitie:
        if element in (' ', ',', '-', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            rezultat += element
        else:
            rezultat += dict3decrypt[element]
    return rezultat



if __name__ == "__main__":
    propozitie = input('introduceti o propozitie:')
    c1 = cript_hash(propozitie)
    print(c1)
    c2 = decript_hash(c1)
    print(c2)
