class Student:
    collname = "RSET"
    def setvalue(self,fname,lname,age,course):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course= course
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.course,Student.collname)

st1 = Student()
st1.setvalue('Jake','c',29,'AI')
st1.printvalue()

st2=Student()
st2.setvalue('Jaske','e',29,'AI')
st2.printvalue()

st3=Student()
st3.setvalue('Jadke','w',9,'AI')
st3.printvalue()

st4=Student()
st4.setvalue('Jaqke','b',29,'AI')
st4.printvalue()