'''Alternative code for finding the
    most used character in a string.'''

s=input('Enter your message: ')
L=len(s)
s=s.replace(' ','')
s=s.strip()
s=s.lower()

l=[]
d={}
for i in s:
    c=s.count(i)
    l.append(c)
    d[c]= i
m= max(l)
print('The lenght of your message is',L,end='.\n')
print('The most common letter in your message is', d[m]+'.')
