class Student:
    def __init__(self,id,fname,lname,age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age)

stu = Student(1,'Jake','M',20)
stu.printvalue()