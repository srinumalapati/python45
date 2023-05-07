81. Please write a program to generate a list with 5 random numbers between 
100 and 200 inclusive.
import random

mylist = []

for i in range(0,100):
    x = random.randint(1,10)
    mylist.append(x)

print(mylist)