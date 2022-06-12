explanation="""Variable Not Being Recognized By Function Trivial

The following code causes an error:

def main():
    x= 5
   trivial()

def trivial():
    print(x)

main()

But can be corrected by defining x as a GLOBAL VARIABLE:

x=5

def main():
    x=5
    trivial()

def trivial():
    print(x)

main()

A proper output will now be demonstrated..."""

x= 5

def main():
    x= 5
    trivial()

def trivial():
    print(x)

print(explanation)
print("\n")
main()
