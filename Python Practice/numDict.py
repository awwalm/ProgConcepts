'''Tiny Number Dictionary'''

def numDict():
    wholeNum= dict()
    wholeNum['one']=int(1)
    wholeNum['two']=int(2)
    wholeNum['three']=int(3)
    wholeNum['four']=int(4)
    return wholeNum

def main():
    integers=numDict()
    print(integers['one'])
    print(integers['four'])

main()
