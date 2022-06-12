firstNumber= eval(input('Enter first number: '))
secondNumber= eval(input('Enter second number: '))
thirdNumber= eval(input('Enter third number: '))

max= firstNumber
if secondNumber > max:
    max= secondNumber
if thirdNumber > max:
    max= thirdNumber
print('The largest number is ', max, '.', sep='')
