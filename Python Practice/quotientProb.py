def quotientProb(x, y):
        quotient=x//y
        remainder=x%y
        print('The quotient of ', x, ' and ', y, ' is ', quotient, ' with a remainder of ', remainder, '.', sep='')

def main():
        quotientProb(17,15)
        quotientProb(452,75)
        a=int(input('Enter a number: '))
        b=int(input('Enter a divisor: '))
        quotientProb(a, b)

main()
