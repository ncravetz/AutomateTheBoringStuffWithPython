# Comma Code (Chapter 4)

#Takes a list value and returns a string with all the items separated by a comma and an 'and' before the last one

def commaCode(userList):
        for i in range (len(userList)):
                if userList[i] != userList[-2]:
                        print(userList[i] + ', ', end="")
                else:
                        print(userList[-2] + ' and ' + userList[-1], end="")
                        break
		


	

#print('Give me a list')
#userInput = input()

eggs=['blanco', 'marron', 'roto']

commaCode(eggs)

