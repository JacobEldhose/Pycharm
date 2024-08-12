# def fact_1():
#     num = int(input("Enter the number "))
#     fact = 1
#     for i in range(1, num+1):
#         fact = fact * i
#     print(fact)
#
#
# def fact_2(num):
#     fact = 1
#     for i in range(1, num+1):
#         fact = fact * i
#     print(fact)
#
#
# def fact_3(num):
#     fact = 1
#     for i in range(1, num+1):
#         fact = fact * i
#     return fact
#
#
# fact_1()
# num = int(input("Enter the number "))
# fact_2(num)
#
# print(fact_3(num))
def r_fact(num1):
    if num1 == 1:
        return num1
    else:
        fact = r_fact(num1 - 1) * r_fact(num1)
        return fact


print(r_fact(int(input("Enter the number"))))
