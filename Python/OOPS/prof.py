class Personel_data:
    def data(self, id, fname, lname, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        # print(self.id,self.fname,self.lname,self.age)
class Professional_data(Personel_data):
    def print_data(self, prof, dept, salary, loc):
        self.dept = dept
        self.prof = prof
        self.salary = salary
        self.loc = loc
        print(self.id,self.fname,self.lname,self.age,self.prof,self.dept,self.salary,self.loc)

obj = Professional_data()
obj.data(1,"First","Last",20)
obj.print_data("ai", "student", 10000, "kakkanad")