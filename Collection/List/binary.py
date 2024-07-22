lst = [23, 34, 54, 65, 76, 87, 12]
search = int(input("enter the element to be searched: "))
lst.sort()
flag = 0
first = 0
last = len(lst)-1
while first <=last:
    mid = (first + last)//2
    if lst[mid] == search:
        print(f"{search} found at position {mid}")
        flag = 1
        break
    elif search < lst[mid]:
        last = mid-1
    elif search > lst[mid]:
        first = mid+1

if flag == 0:
    print("Item not found")
