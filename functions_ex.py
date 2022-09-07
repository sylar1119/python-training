# irjátok meg a signum függvényt !
# ha a szám kisebb mint 0 akkor -1 et ad
# ha 0 akkor 0
# ha nagyobb mint 0 akkor 1et

def signum(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    elif n == 0:
        return 0
print(signum(-100))

#írjatok egy függvényt, ami vár egy egész számot és visszaadja és vissza adja annak abszolut értékét
#írjatok egy függvényt amely várja a téglalap a és b oldalát és vissza adja a területet
#írjatok egy függvényt amely várja a téglalap a és b oldalát és vissza adja a kerületet
#írjatok egy függvényt amely vár két számot ami vissza adja kettő közül a nagyobbat 
#írjatok egy függvényt ami kiirja hogy páros v páratlan a szám

def absolute(n):
    if n <= 0:
        return (-n)
    else:
        return (n)
print(absolute(1))

print("------")

def area(i, j):
    return i * j
print(area(2, 5))

print("-----")

def kerul(i, j):
    return (i + j) * 2
print(kerul(2, 5))


def nagyobb(i, j):
    if i>0:
        return i
    else:
        return j
print(nagyobb(10, 5))

def parosoderparatlan(i):
    if i %2 == 0:
        return("páros")
    else:
        retrun("páratlan")
print(parosoderparatlan(10))