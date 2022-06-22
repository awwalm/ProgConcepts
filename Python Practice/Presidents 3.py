
def textinlist():
    infile= open('Presidents.txt', 'r')
    listPres= [line.rstrip() for line in infile]
    infile.close()
    print(listPres)

    outfile= open('Presidents.txt', 'w')
    outfile.write(str(listPres))
    outfile.close()

textinlist()
