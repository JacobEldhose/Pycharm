pattern = 'ABCDFBCDABR'
dic = {}

for i in pattern:
    if i in dic:
        print(f"Recursive character us {i}")
        break
    else:
        dic[i]=1