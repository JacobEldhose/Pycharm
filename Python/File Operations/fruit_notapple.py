f = open('fruits', 'r')
f1 = open('fruit_not_apple', 'w')
for i in f:
    if i.rstrip('\n') == 'apple':
        pass
    else:
        f1.write(i)
