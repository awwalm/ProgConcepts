def futureValue(p, r, m, t):
    i= r/m
    n= m*t
    amount= p * ((1+i) **n)
    return amount

p= eval(input('Enter amount deposited: '))
r= eval(input('Enter annual rate of interest in decimal form: '))
m= eval(input('Enter number of times interest is compounded per year: '))
t= int(input('Enter number of years: '))
print('Balance after', t, 'years: ${0:,.2f}'.format(futureValue(p, r, m, t)))
