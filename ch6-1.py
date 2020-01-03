tableData = [['apples', 'oranges', 'cherries', 'bannanas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    for x in table:
        for y in range(4):
            data = str(x[y]).rjust(10)
            print(data , end=" ")
        print("") # used only for new line character
printTable(tableData)