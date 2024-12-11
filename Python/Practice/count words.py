def count_word(word):
    s = word.split()
    return len(s)

def count_element(word):
    count = 0
    for i in range(len(word)):
        if word[i] != ' ':
            count += 1
    return count
s="i love learning"
print(count_word(s))
print(count_element(s))