sentence = "In 1984 there were 13 instances of a protest ewith over 1000 people attending"
lst = [i for i in sentence.split() if len(i)<=4]
print(lst)