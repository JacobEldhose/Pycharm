sentence = "my name is jacob eldhose"
v = "aeiou "
lst = [i for i in sentence if i not in v]
print(len(lst))
