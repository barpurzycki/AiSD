#Zad 1
x = 'B'
y = 'Purzycki'
def fun1(im, nazw):
    return im+'.'+nazw
print(fun1(x, y))

#Zad 2
x = 'bartosz'
y = 'purzycki'
def fun2(im, nazw):
    return im[0].capitalize()+'.'+nazw.capitalize()
print(fun2(x, y))

#Zad 3
x = '20'
y = '22'
z = 21
def fun3(a, b, c):
    return int(str(a)+str(b))-c
print(fun3(x, y, z))

#Zad 4
x = 'bartosz'
y = 'purzycki'
def fun4(im, nazw, funkcja):
    return funkcja(im, nazw)
print(fun4(x, y, fun2))

#Zad 5
a = 10
b = 2
def fun5(x, y):
    if x > 0 and y > 0 and y != 0:
        return x/y
print(fun5(a, b))

#Zad 6
suma=0
for i in range(0,100):
    suma += int(input("Podaj liczbę:"))
    print("Aktualna suma wynosi:", suma)
    if suma < 100:
        continue
    break

#Zad 7
lista = ["a","b","c","d"]
print(lista)
def fun7(krotka):
    return tuple(krotka)
print(fun7(lista))

#Zad 8
lista=[]
for x in range(5):
    a=input("Podaj wartość:")
    lista.append(a)
krotka=tuple(x for x in lista)
print(krotka)

#Zad 9
def fun9(x):
    return{
        1:'Poniedziałek',
        2:'Wtorek',
        3:'Środa',
        4:'Czwartek',
        5:'Piątek',
        6:'Sobota',
        7:'Niedziela',
    }.get(x,'Zły dzień tygodnia')
print(fun9(6))

#Zad 10
def fun10(tekst):
    for x in range(int(len(tekst)/2)):
        if(tekst[x]!=tekst[(len(tekst)-1)-x]):
            return False
    return True
print(fun10('kajak'))
print(fun10('kajal'))
