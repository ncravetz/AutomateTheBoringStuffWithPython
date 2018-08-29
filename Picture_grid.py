# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
	 ['.', 'O', 'O', '.', '.', '.'],
	 ['O', 'O', 'O', 'O', '.', '.'],
	 ['O', 'O', 'O', 'O', 'O', '.'],
	 ['.', 'O', 'O', 'O', 'O', 'O'],
	 ['O', 'O', 'O', 'O', 'O', '.'],
	 ['O', 'O', 'O', 'O', '.', '.'],
	 ['.', 'O', 'O', '.', '.', '.'],
	 ['.', '.', '.', '.', '.', '.']]




# Hay que ir agarrando el x elemento de cada sub-lista, despues el elemento x+1 de cada sub-lista

def picture(gridList):

	for i in (range(len(gridList[0]))):
		print()
		for n in (range(len(gridList))):
				print(gridList[n][i], end="")
			



picture(grid)
