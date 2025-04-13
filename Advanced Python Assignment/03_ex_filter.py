letters = ['a', 'b', 'c', 'e', 'i']
vowel = filter(lambda x:x in "aeiou", letters)
print(list(vowel))