class Employee:
    prof = "Developer"
    company_name = "Luminar"
    def setvalue(self,id,fname,lname,age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
    def printvalue(self):
        print(self.fname,self.lname,self.age,Employee.prof,Employee.company_name)

emp1 = Employee()
emp1.setvalue(1,'jake','k',20)
emp1.printvalue()

emp2 = Employee()
emp2.setvalue(2,"Ammu",'e',21)
emp2.printvalue()