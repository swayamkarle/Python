# def fun(variable):
#     letters = ['a','e','i','o','u']
#     if(variable in letters):
#         return True
#     else:
#         return False
# sequence=['P','y','t','h','o','n','i','c']
# filtered=filter(fun, sequence)
# print(filtered)
# print("The filtered letters are:")
# for s in filtered:
#     print(s)

# def divbythree(num):
#     if(num % 3 ==0):
#         return True
#     else:
#         return False
# # numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# numbers = (range(1, 21,1))
# # print(numbers)
# filtered= filter(divbythree, numbers)
# for s in filtered:
#     print(s)
    
    
    
l1=[1,'a',0,False,True,'0']
flist= filter(None, l1)
print("The filtered elements are:")
for e in flist:
    print(e)