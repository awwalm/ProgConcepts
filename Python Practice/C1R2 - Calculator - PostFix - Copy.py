class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])


def eval_postfix(expr):
    ################################
    if expr == '...':
        import sys
        print('Program Terminated.')
        sys.exit()
    ################################       

    #if len(expr) < 2:
    if expr.isdigit():
        print(expr)
        replay()
        #else:
         #   print('Invalid Syntax!\nOperation not properly specified.\n')
          #  replay()
            
    if '**' in expr:
        print('Indices, Powers and Square Root not supported.\n')
        replay()
        
    if '.' in expr:
        print("Must express decimals in fractions first...",
              "\ne.g: 1.5 = 3 2 /, 0.1 = 1 10 /\n")
        replay()
    
    if '/' not in expr:
        if '*' not in expr:
            if '+' not in expr:
                if '-' not in expr:
                    print('Invalid Syntax!'
                          '\nNo Operators Specified From Last Input.\n')
                    replay()

    OP = '/','*','+','-'
    S=[]
    J=[]
    excount=expr.split(' ')
    for y in excount:
        for i in OP:
            if y == i:
                ss=excount.count(i)
                S.append(ss)
    SS=len(S)
    for j in excount:
        if j.isdigit():
            jj=excount.count(j)
            J.append(jj)
    JJ=len(J)
    if SS >= JJ:
        print('Invalid syntax or Operators out of range.\n')
        replay()
    Q=int(JJ-SS)
    if Q > 1:
        print('Operators not in range.\n')
        replay()

    else:
        pass

    import re
    token_list = re.split('([^0-9])', expr)
    stack= Stack()

    if token_list[-1].isdigit()is True:
        print('Expression must be Post Fix type only!\n')
        replay()

    if token_list[0].isdigit() is False:
        print('Invalid Syntax!\n')
        replay()

    for token in token_list:
        if token == "" or token == " ":
            continue            

        badSyntax= ["!", "?", "#", "$", "&", "(", ")", "£", "¬", "^", '"', "'",
                    "[", "]", "=", "{", "}", ";", ":", ">","<", "," , "`", "¦"]
        #badSyntax library requires regular expansion to avoid invalid input!
        #can be optionally imported from txt file in future.
        for syntax in badSyntax:
            if token == syntax:
                print('Invalid Syntax!\n')
                replay()

        if token.isalpha():
            print('Invalid Input! Must contain numbers and operators ONLY.\n')
            replay()

        if token == "/":
            quotient1 = stack.pop()
            quotient2 = stack.pop()
            if quotient1 == 0:
                print('Division By Zero Impossible!\n')
                replay()
            quotient = quotient2 / quotient1
            stack.push(quotient)

        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)            

        elif token == "+":
            Sum = stack.pop() + stack.pop()
            stack.push(Sum)

        elif token == "-":
            difference = -stack.pop() + stack.pop()
            stack.push(difference)

        else:
            stack.push(int(token))

    return print(stack.pop())

def replay():
    while 1>0:
        eval_postfix(input('Enter a post fix expression: '))

replay()
    



    
