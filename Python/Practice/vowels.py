def words_with_vowels(word):
    vow = 'aeiou'
    lst = []
    for i in word.split():
        for j in i:
            if j in vow:
                lst.append(i)
                break

    return lst
word = 'You have no rhythm'
print(words_with_vowels(word))