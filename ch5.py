def displayInventory(Inventory):
    print(Inventory)
    total = 0
    for x,y in Inventory.items():
        print(x, end =' ')
        print(y)
        total = total + y
    print("The total amount of items is:" + str(total))
def addToInventory(inventory, addedItems):
    for x in addedItems:
        if x in inventory:
            inventory[x] = inventory[x] + 1
        else:
            inventory[x] = 1
            
Inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(Inventory, dragonLoot)

displayInventory(Inventory)