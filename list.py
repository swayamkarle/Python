l=[]
for i in range (10):
    x=input("Enter  marks:")
    l.append(int(x))
a=0
b=0
c=0
d=0
e=0
for x in l:
    if(x>=0 and x<=39):
        a+=1
    elif(x>=40 and x<=59):
        b+=1
    elif(x>=60 and x<=69):
        c+=1
    elif(x>=70 and x<=89):
        d+=1
    elif(x>=90 and x<=100):
        e+=1

print("Number of students with marks >0 and <39:",a)
print("Number of students with marks >40 and <59:",b)
print("Number of students with marks >60 and <69:",c)
print("Number of students with marks >70 and <89:",d)
print("Number of students with marks >90 and <100:",e)