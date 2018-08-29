#Fantasy Game Inventory 

chest ={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
	totalItems = 0
	print('Inventory:')
	for k, v in inventory.items():
		print(k + ': ' + str(inventory[k]))
		totalItems= totalItems + int(v)
	print('Total inventory: '+ str(totalItems))	
	print()




def addToInventory(inventory, addedItems):
	for i in addedItems:
		if i in inventory.keys():
			inventory[i] = inventory[i] + 1
		else:
			inventory[i] = 1	


displayInventory(chest)


addToInventory(chest, dragonLoot)


displayInventory(chest)
