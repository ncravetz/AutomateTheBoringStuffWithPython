#! Python3

# Take a list of lists and prints a well arranged table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
 			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
	itemLength = [0] * len(table)
	colWith = [0] * len(table)

	for i in range(len(table)):
		itemLength[i] = [0] * len(table[i]) 

		for k in range(len(table[0])):
			itemLength[i][k] = len(table[i][k])

	for x in range(len(colWith)):
		colWith[x] = max(itemLength[x])
	
	for z in range(len(table[0])):
		print()
		for e in range(len(table)):
			print(tableData[e][z].rjust(colWith[e]+1), end="")




# TODO: find longest len of each list, print with rjust(len of max), print each value 1, each value 2, etc



printTable(tableData)
