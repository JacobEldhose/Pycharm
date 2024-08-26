ls = [3,45,1,7,2,53,4]
search = 45
ls = sorted(ls)
first = 0
last = len(ls)
print(ls)

while(first <= last):
    mid = (first + last) // 2
    if search == ls[mid]:
        print("f at ",mid)
        break
    elif(ls[mid]<=search):
        first = mid+1
    elif(search<=ls[mid]):
        last = mid -1
    else:
        print("not fouinf")
        break