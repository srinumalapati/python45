def factorial(n):
    value = 1
    for i in range(1, n+1):
        value = value * i
    return value
number = int(input("Type a number: ")
print(factorial(number))