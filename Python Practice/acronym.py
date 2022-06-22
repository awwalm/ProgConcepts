'''acronym.py'''
s=input('type to abbreviate: ')
s=str(s)
s=s.upper()
s=s.split(' ')
for i in s:
    if i.isalpha():
        ls= str(i)
        print(ls[0],end='')
    if i.isdigit():
        print(i, end='')
    else:
        pass
