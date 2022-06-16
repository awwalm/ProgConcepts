def chc1():
   Chc=input('Choice: ')
   return Chc

def loopProgram():
   geekTrans()
   nextStep()

geekDict= dict()
geekDict['404']= '404 means clueless. From the web error message 404, meaning page not found.'
geekDict['wifi']= 'WiFi is a form of Wireless Area Networking that converts Internet Connectivity into Radio Waves signals.'
geekDict['ip']= 'IP stands for Internet Protocol. A platform of basis that allows connection to a server.'
geekDict['dos']= 'DOS stands for Disk Operating System. An historic OS that uses comand line interface.'

def geekTrans():
   print("\n")
   print("\t", 'Geek Translator')
   print("\n")
   print("\t", '0 - Quit')
   print("\t", '1 - Look Up a Geek Term')
   print("\t", '2 - Add a Geek Term')
   print("\t", '3 - Redefine a Geek Term')
   print("\t", '4 - Delete a Geek Term')
   print("\n")
   chc1()

geekTrans()
print("\n")
def nextStep():
    for Chc:
        print(geekDict[input('What term do you want me to translate?: ')])
    while 1>0:
       loopProgram()

nextStep()
