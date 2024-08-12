class Person:
    def setvalue(self,fname,lname,age,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.loc=loc
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.loc)

per1 = Person()
per1.setvalue('vinay','k',28,'ekm')
per1.printvalue()

per2 = Person()
per2.setvalue('vipin','p',20,'ekm')
per2.printvalue()