"""Write a Python program to generate all possible valid identifiers of length n,
where n is provided by the user character of n number is given by the user.
"""


def generate_words(letters):
    results = ['']

    for letter in letters:
        new_results = []
        for word in results:
            for i in range(len(word) + 1):
                new_word = word[:i] + letter + word[i:]
                if new_word not in new_results:
                    new_results.append(new_word)
        results = new_results

    return results


# Example usage
letters = 'abc'
words = generate_words(letters)
print(words)

        