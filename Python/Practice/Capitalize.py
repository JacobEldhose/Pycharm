def cap(word):
    new = []
    for i in word.split():
        new.append(i.capitalize())
    return ' '.join(new)
r="i like learning"
print(cap(r))