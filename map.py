# def square(num):
#     return num**2
# numbers= [1,2,3,4,5]
# squared= map(square, numbers)
# print(list(squared))

# Type Casting using map method 


# l1=["1","3","4","5","6"]
# print(list(map(int, l1)))

# first=[1,2,3]
# second=[4,5,6]
# print(list(map(pow,first,second)))

# str1 = ["applying","map", "on", "strings"]
# print(list(map(str.capitalize,str1)))
# print(list(map(str.upper,str1)))
# print(list(map(str.lower,str1)))


# REDUCE 


def add(a,b):
    result=a+b
    print(f"{a} + {b} = {result}")
    return result
from functools import reduce 
numbers=[0,1,2,3,4]
reduce(add,numbers)
print(reduce(add,numbers,100))