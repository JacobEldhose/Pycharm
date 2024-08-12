""" Functional Programming """

# Re-usability

# Traditional approach

# Modern approach

# lambda
# map
# filter
# list comprehension

"""
lambda : anonymous function

syntax
variable_name = lambda arguments : operation
"""
# f = lambda num1, num2: num1 + num2
# print(f(20, 30))

# mul = lambda num1, num2, num3 : num3 * num2 * num1
# print(mul(10,20,30))

# mul = lambda num1 : num1 ** 2
# print(mul(10))

"""
map
syntax
variable_name = list(map(function, iterable)) 

filter
syntax
variable_name = list(filter(function, iterable))
"""
lst = [1, 2, 3, 4, 5, 6, 7]

# f = list(map(lambda num :num**2,lst))
# print(f)

f = list(filter(lambda num : num**2,lst))
print(f)