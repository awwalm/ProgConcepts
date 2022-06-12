word= input('Enter a word: ')

def occurringVowels(word):
    word= word.upper()
    vowels= ('A', 'E', 'I', 'O', 'U')
    includedVowels= []
    for vowel in vowels:
        if (vowel in word) and (vowel not in includedVowels):
            includedVowels.append(vowel)
    return includedVowels

listofVowels= occurringVowels(word)
print('The following vowels occur in the word: ', end='')
stringOfVowels= " ".join(listofVowels)
print(stringOfVowels)
