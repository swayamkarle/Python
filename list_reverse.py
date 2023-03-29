a=[9,9,1,9,3,2]
b=a.copy()
b.reverse()
c=[]

for i in range(len(a)):
    x=a[i]+b[i]
    c.append(x)
    
print(c)

