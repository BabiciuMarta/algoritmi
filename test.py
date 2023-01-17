import math

l = [1, 3, 4, 5, 7, 9, 12, 15, 8, 2]


def suma():
    s = 0
    for i in range(len(l)):
        if i < 3 or i > 7:
            s += l[i]


def cautare():
    val = int(input())
    for i in range(len(l)):
        if l[i] == val:
            print("patrat", l[i]**2)


def cautare_salt():
    l = [2, 3, 10, 20, 25, 30, 100, 50, 40, 27, 5, 18, 60]
    l.sort()
    n = len(l)
    salt = int(math.sqrt(n))
    val = int(input()) # 60
    # identificam portiunea de lista in care se gaseste valoarea cautata
    # st si st+salt
    for i in range(0, n, salt):
        if l[i] < val:
            st = i
        elif l[i] == val:
            print(i)
        else:
            break

    # efectuez o cautare secventiala pe bucata de lista identificata anterior
    for i in range(st, st+salt):
        if l[i] == val:
            print(i)



if __name__ == "__main__":
    cautare_salt()