"""Write a program that takes inputs  from user and prints the multiplication table of that number"""


num=int(input("Enter the number :"))

for i in range(1,13):
    print(i,"*",num ,"=",num*i)


i=1
while(i<=12):
    print(i, "*", num, "=", num * i)
    i+=1