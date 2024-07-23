"""
List inside a list
"""

lst = [[101, 'jake', 'k', 27, 'python', 1000],
       [102, 'ajay', 'c', 25, 'python', 1300],
       [103, 'don', 'a', 29, 'bigdata', 2300],
       [104, 'kanye', 'c', 23, 'bigdata', 2000],
       [105, 'jerome', 'g', 24, 'python', 1800],
       [106, 'aswin', 'r', 28, 'bigdata', 1850],
       [107, 'anu', 's', 29, 'python', 2000]]
"""<------------------------------------------------------------------------>"""
# Age above 27 f_name l_name age prof
# for i in lst:
#     if i[3] > 27:
#         print(i[1:5])
"""<------------------------------------------------------------------------>"""
# Age equal to 25 f_name age salary
# for i in lst:
#        if i[3] == 25:
#               print(i[1::2])
"""<------------------------------------------------------------------------>"""
# bigdata prof f_name l_name age prof sa;ary
# for i in lst:
#        if i[4] == 'bigdata':
#               print(i[1:])
"""<------------------------------------------------------------------------>"""
# salary above 1500 f_name l_name age prof
# for i in lst:
#        if i[5]>1500:
#               print(i[1:5])
"""<------------------------------------------------------------------------>"""
# age above 27 and prof bigdata f_name l_name age
# for i in lst:
#        if i[3]>27 and i[4] == 'bigdata:
#               print(i[1:4])
"""<------------------------------------------------------------------------>"""
# Total salary
# salary = 0
# for i in lst:
#        salary += i[-1]
# print(salary)
"""<------------------------------------------------------------------------>"""
