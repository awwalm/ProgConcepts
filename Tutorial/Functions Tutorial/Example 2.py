def firstName(fullName):
    firstSpace= fullName.index(" ")
    givenName= fullName[:firstSpace]
    return givenName
print()
fullName= input("Enter a person's full name: ")
print("First name:", firstName(fullName))
