import time
print('WELCOME TO MY CALCULATOR')
time.sleep(1)

def main() :
    num1 = int(input('Enter the First number... '))
    num2 = int(input('Enter the second number... '))
    
    op = input("""what operation would you like to do ?
1 = Addition
2 = Subtraction
3 = Multipication
4 = Division
""")

    if op == '1':
        print (num1, '+' , num2, '=')
        time.sleep(1)
        print (num1 + num2)
        time.sleep(2)
        main()

    if op == '2':
        print(num1, '-' , num2, '=')
        time.sleep(1)
        print (num1 + num2)
        time.sleep(2)
        main()

    if op == '3':
       print(num1, '*' , num2, '=')
       time.sleep(1)
       print (num1 * num2)
       time.sleep(2)
       main()
       
    if op =='4':
       print(num1 , '/' , num2, '=')
       time.sleep(1)
       print(num1 / num2)
       time.sleep(2)
       main()

    else:
        print('ERROR INVALID INPUT PLEASE TEXT AGAIN')
        time.sleep(1)
        main()

main()

    
