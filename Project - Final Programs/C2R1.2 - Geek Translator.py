
geekDict= dict()
geekDict['404']= '404 means clueless. From the web error message 404, meaning page not found.'
geekDict['WIFI']= 'WiFi is a form of Wireless Area Networking that converts Internet Connectivity into Radio Waves signals.'
geekDict['IP']= 'IP stands for Internet Protocol. A platform of basis that allows connection to a server.'
geekDict['DOS']= 'DOS stands for Disk Operating System. An historic OS that uses comand line interface.'

chc=''
while chc!='0':
   print("\n")
   print("\t", 'Geek Translator')
   print("\n")
   print("\t", '0 - Quit')
   print("\t", '1 - Look Up a Geek Term')
   print("\t", '2 - Add a Geek Term')
   print("\t", '3 - Redefine a Geek Term')
   print("\t", '4 - Delete a Geek Term')
   print("\n")
   chc= input('Choice: ')

     
   if chc == '1':
      lookUp= input('What term do you want me to translate?: ').upper()
      if lookUp in geekDict:
         print(geekDict[lookUp])

         
      else:
         print('That Word is not available!')
         

      
   elif chc == '2':
      newWord= input("Enter a geek word you'd like to add: ").upper()
      if newWord in geekDict:
         print("The word you're attempting to add already exists. You can look it up by selecting choice 1.")
         
         

      else:
         geekDict[newWord]= input('Enter a brief definition for your new word: ')
         print(newWord, ' has been added to the dictionary. You can look it up anytime.')



   elif chc == '3':
      redefWord= input('Enter an EXISTING word to redefine or edit: ').upper()
      if redefWord in geekDict:
         geekDict[redefWord]= input('Enter a new definition for this Geek Word: ')

      else:
         print("The Geek Word doesn't exist in the Dictionary!")


   elif chc == '4':
      delWord= input('Enter an EXISTING geek word to delete from the Translator library: ').upper()
      if delWord in geekDict:
         del(geekDict[delWord])
         print(delWord, ' has been removed from the dictionary.')

      else:   
         print('Only existing words can be deleted!')


   else:
      if chc == '0':
         input('Press Enter To Exit')



