f = open('content', 'r')
w = open('cont_copy', 'w')

for i in f:
    w.write(i)
