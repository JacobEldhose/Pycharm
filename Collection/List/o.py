lst = []

for i in range(1, 51):
    lst.append(i)

eve_lst = []
odd_lst = []

for i in lst:
    if i % 2 == 0:
        eve_lst.append(i)
    else:
        odd_lst.append(i)

eve_sum = 0
odd_sum = 0

# def sums(lst):
#     sums = 0
#     for j in lst:
#
#         sums = sums + j
#     return sums

print(lst,'\n',sum(lst))
print(f"Sum of even numbers {eve_lst} = \n{sum(eve_lst)}")
print(f"Sum of odd numbers {odd_lst} = \n{sum(odd_lst)}")