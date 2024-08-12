dic = {'bike':500,'bus':5000,'car':2500,'cycle':100,'jeep':3000}

lst = [i for i in dic if dic[i]>2000]
print(lst)