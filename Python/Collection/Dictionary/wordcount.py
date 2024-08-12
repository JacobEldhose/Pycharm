para = 'cat rat cat cart rat car bar bet bat rat cat'
para = para.split()
dic = {}
for i in para:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
