 Write a program which accepts a sequence of comma-separated numbers 
from console and generate a list and a tuple which contains every 
number.Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

numbers = input("Type in numbers seperated only by a comma :")
numbers_split = numbers.split(',')

number_tuple = tuple(numbers_split)

print(number_tuple)
print(numbers_split)