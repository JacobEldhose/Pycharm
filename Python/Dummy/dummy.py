if __name__ == '__main__':
    N = int(input())
    L =[]
    for j in range(N):
        cond = input()
        if "insert" in cond:
            cond, i, e = cond.split()
            L.insert(int(i), int(e))
        elif "remove" in cond:
            cond, e = cond.split()
            L.remove(int(e))
        elif "append" in cond:
            cond, e = cond.split()
            L.append(int(e))
        elif "sort" in cond:
            L.sort()
        elif "pop" in cond:
            L.pop()
        elif "reverse" in cond:
            L.reverse()
        elif "print" in cond:
            print(L)
