print("============================")

def rec(i):
    if i<0:
        return

    print(f'i: {i}')

    rec(i - 1)

rec(10)

print("============================")

#Zad 1

def numbers(n):
    if(n<0):
        return
    print(n)
    numbers(n - 1)

numbers(5)

print("============================")

#Zad 2

def fib(n):
    if(n == 0):
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return  (fib(n-1) + fib(n-2))

print(fib(10))

print("============================")

#Zad 3

def power(number, n):
    if n == 0:
        return 1
    elif n == 1:
        return number
    else:
        return number * power(number, n - 1)

print(power(3, 3))

print("============================")

#Zad 4

def reverse(txt:str):
    if len(txt) == 0:
        return txt
    else:
       return reverse(txt[1:])+txt[0]

print(reverse("123456789"))

print("============================")

#Zad 5

def factorial(n):
    if(n > 1):
        return n * factorial(n-1)
    else:
        return 1

print(factorial(5))

print("============================")

#Zad 6

def prime(n:int, i=2) -> bool:
    if n==i:
        return True
    elif n%i==0:
        return False
    return prime(n,i+1)

print(prime(5))

print("============================")

#Zad 7

def n_sums(liczby:int, lista=[]):
    if liczby > 100:
        return lista
    temp = [int(x) for x in str(liczby)]
    print(temp)
    if sum(temp[::2]) == sum(temp[1::2]):
        lista.append(liczby)
    return n_sums(liczby + 1, lista)
print(n_sums(3))

print("============================")

#Zad 9

def remove_duplicates(txt:str) -> str:
    if len(txt) == 1:
        return txt[0]
    elif txt[0] != txt[1]:
        return txt[0] + remove_duplicates(txt[1:])
    else:
        return remove_duplicates(txt[1:])

print(remove_duplicates("1233456"))

print("============================")




