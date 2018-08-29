# The Collatz Sequence

def collatz(number):
	if number%2 == 0:
		number=number//2
		print(number)
		return number

	elif number == 0:
		number= 1	
		print(number)
		return number
	

	else:
		number=(3*number) +1	
		print(number)
		return number
	



# Ask player for number 

print('Give me a number')
playerNumber = int(input())



while playerNumber != 1:
        if playerNumber != 1:
                playerNumber=collatz(playerNumber)
                
        else:
                print(1)               




