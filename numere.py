def adunarecifre2():
    print("Introduceti va rog un numar de doua cifre:")
    a = input()
    a = int(a)
    z = a // 10
    u = a % 10
    print("Suma zecilor si unitatilor este:", z+u)


def adunarecifre3():
    print("Introduceti va rog un numar de 3 cifre:")
    b = input()
    b = int(b)
    s = b // 100
    z = b // 10 % 10
    u = b - (s*100+z*10)
    print("Suma sutelor, zecilor si a unitatilor este:", s+z+u)


def capetepicioare():
    print("Introduceti numarul de gaini:")
    g = int(input())
    print("Introduceti numarul de oi:")
    o = int(input())
    print("Numarul de capete este:", g+o, " , iar numarul de picioare este: ", 2*g + 4*o)


def capetepicioare2():
    print("Introduceti numarul de picioare:")
    p = int(input())
    print("Introduceti numarul de capete:")
    c = int(input())
    o = (p-(2*c))//2
    g = c - o
    print("Numarul de gaini este:", g, " , iar numarul de oi este: ", o)


def eliminarecifra():
    print("Introduceti un numar natural de 3 cifre:")
    n = int(input())
    s = n // 100
    z = n // 10 % 10
    u = n - (s*100+z*10)
    print("Numarul rezultat din eliminarea cifrei din mijloc este:", str(s)+str(u))


def ariesivolumcub():
    print("Introduceti latura cubului:")
    l = int(input())
    s = 6 * l * l
    v = l ** 3
    print("Suprafata cubului este:", s, "iar volumul este:", v)


if __name__ == "__main__":
    adunarecifre2()
    adunarecifre3()
    capetepicioare()
    capetepicioare2()
    eliminarecifra()
    ariesivolumcub()
