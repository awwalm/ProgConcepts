str1= input('Enter a message: ').upper()
print("\n")

str2= "The most common letter in the English language, 'e', is in your message."
str3= "The most common letter in the English language, 'e', is not in your message."
str4= print('The length of your message is: ',len(str1))
str5= 'You have used all the english vowels.'
str6= "You have'nt used ALL the english vowel letters. However, you may have used some."

str4
print("\n")

#A good example for str1 user prompt is the chorus from the Michael Jackson song...
#'Smooth Criminal'; "Annie, are you okay?"
#It has all vowels

def isVowelWord(word):
    vowels= ['A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

if isVowelWord(str1):
    print(str5)
else:
    print(str6)

if 'E' in str1:
    print(str2)
else:
    print(str3)

print("\n")

input('Press the enter key to exit.')
