def discounter():

    price= eval(input('Price? :'))
    discount= eval(input('Disount percentage? :'))
    percent= discount/100
        
    newPrice= price - (percent * price)
    print('{0:.2f}'.format(newPrice), '\n')

while 1>0:
    discounter()
