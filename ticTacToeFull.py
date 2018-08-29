# TicTacToe whit dictionaries

theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
			'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
			'low-L':' ', 'low-M':' ', 'low-R':' '}


def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])



turn = 'X'

while list(theBoard.values()).count (' ') > 0:
	printBoard(theBoard)

#Jugador inserta ficha

	print('Turn for ' + turn + '. Move on which space?')
	move = input()
	# Que no se pueda reemplazar lo ya asignado
	if theBoard[move] == ' ':
		theBoard[move] = turn
	




	
		# Revisar si uno gano
		if theBoard['top-L']==theBoard['top-M']==theBoard['top-R']!= ' ':
			print('Player ' + theBoard['top-L'] + ' wins')
			break
		if theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R']!= ' ':
			print('Player ' + theBoard['mid-L'] + ' wins')
			break
		if theBoard['low-L']==theBoard['low-M']==theBoard['low-R']!= ' ':
			print('Player ' + theBoard['low-L'] + ' wins')
			break
		if theBoard['top-L']==theBoard['mid-L']==theBoard['low-L']!= ' ':
			print('Player ' + theBoard['top-L'] + ' wins')
			break		
		if theBoard['top-M']==theBoard['mid-M']==theBoard['low-M']!= ' ':
			print('Player ' + theBoard['top-M'] + ' wins')
			break
		if theBoard['top-R']==theBoard['mid-R']==theBoard['low-R']!= ' ':
			print('Player ' + theBoard['top-R'] + ' wins')
			break
		if theBoard['top-L']==theBoard['mid-M']==theBoard['low-R']!= ' ':
			print('Player ' + theBoard['top-L'] + ' wins')
			break
		if theBoard['top-R']==theBoard['mid-M']==theBoard['low-L']!= ' ':
			print('Player ' + theBoard['top-R'] + ' wins')
			break



		# Si nadie gano cambia de jugador
		elif turn == 'X':
			turn = 'O'
		else:
			turn = 'X'


	else:
		print('That place is taken. Try another one')		


printBoard(theBoard)	


