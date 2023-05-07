82. Please write a program to randomly generate a list with 5 even numbers 
between 100 and 200 inclusive.

import random
print(random.sample([i for i in range(1,100) if i%2==0], 5))
