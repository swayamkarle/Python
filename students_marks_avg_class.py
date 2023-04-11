class Student:
    def __init__(self,name,roll_no,m1,m2,m3,m4,m5,address) :
        self.name=name
        self.roll_no=roll_no
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
        self.address=address

    def get_data(self):
        print("Name:",self.name)
        print("Rol no:",self.roll_no)
        print("Address:",self.address)
        print("Marks 1:",self.m1)
        print("Marks 2:",self.m2)
        print("Marks 3:",self.m3)
        print("Marks 4:",self.m4)
        print("Marks 5:",self.m5)
        print("percentage:",(m1+m2+m3+m4+m5)/5)

Students=[]

n=int(input("Enter the number of Students:"))

for i in range(n):
    name=input("Enter name:")
    rollno=int(input("Enter rollno:"))
    address=input("Enter address:")
    m1=float(input("Enter marks 1:"))
    m2=float(input("Enter marks 2:"))
    m3=float(input("Enter marks 3:"))
    m4=float(input("Enter marks 4:"))
    m5=float(input("Enter marks 5:"))
    
    Students.append(Student(name,rollno,m1,m2,m3,m4,m5,address))

for stu in Students:
    stu.get_data()