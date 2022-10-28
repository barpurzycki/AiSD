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

# def reverse(txt:str):
#     if(txt[i] == 0):

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

def prime(n:int):
    if(n != 0):
        if(n % (n - 1) != 0):
            return 1
            prime(n - 1)
        else:
            return 0


print(prime(4))




