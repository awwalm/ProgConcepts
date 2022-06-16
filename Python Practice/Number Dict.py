'''My Own Custom Tiny Number Dictionary'''

def numDict():
    wholeNum= dict()
    wholeNum['zero']=int(0)
    wholeNum['one']=int(1)
    wholeNum['two']=int(2)
    wholeNum['three']=int(3)
    wholeNum['four']=int(4)
    wholeNum['five']=int(5)
    wholeNum['six']=int(6)
    wholeNum['seven']=int(7)
    wholeNum['eight']=int(8)
    wholeNum['nine']=int(9)
    wholeNum['ten']=int(10)
    return wholeNum

def main():
    integers=numDict()
    prompt=input('Enter any number, between zero and ten, in plain words, to express in digits: ')
    print(integers[prompt])
    

main()
