'''Alternative code for finding the
    most used character in a string.'''

s= input('Enter your message: ')
L=len(s)
l=[]
d= {}
for i in s:
    c=s.count(i)
    l.append(c)
    d[c]= i
m= max(l)
print('The lenght of your message is',L,end='.')
print('\nThe most common letter in your message is', d[m]+'.')
