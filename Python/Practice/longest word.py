'''
Write a function that has one parameter and takes a list of words as an argument. The function returns the longest
word from the list.Name the function longest word. The function should return the longest word and the number of letters
in that word. For example, if you pass ['Java, 'JavaScript', 'Python'], your function should return
[10, JavaScript] as the longest word.
'''

def longest_word(word):
    lst = []

    for i in word:
        lst.append([len(i),i])
    print(lst)
    return max(lst)
word = ['Java', 'JavaScript', 'Python']
print(longest_word(word))