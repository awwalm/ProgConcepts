'''Alternative code for finding the
    most used character in a string.'''

s=input('Enter your message: ')
if s == '':
    print('No message detected.')
    import sys
    sys.exit()
else:
    pass
L=len(s)
s=s.strip()
s=s.lower()

l=[]
d={}
for i in s:
    if i.isalpha():
        c=s.count(i)
        l.append(c)
        d[c]= i
    else:
        pass
m= max(l)
print('The lenght of your message is',L,end='.\n')
print('The most common letter in your message is', d[m]+'.')
