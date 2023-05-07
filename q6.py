import math
numbers=input("provide D:")
numbers=numbers.split(',')
result_list=[]
for D in numbers:
    Q=round(math.sqrt(2*50*int(D)/30))
    result_list.append(Q)
print(result_list)    

