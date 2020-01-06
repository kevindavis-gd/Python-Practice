#! python3
# store.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe store.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe store.pyw <keyword> - Loads keyword to clipboard.
#        py.exe store.pyw list - Loads all keywords to clipboard

import shelve
import pyperclip
import sys

#open a shelve file named store and save it to storeShelf
storeShelf = shelve.open('store')

#if there are 3 arguments (0 to 2) and argv[1] is save
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    print(str(pyperclip.paste()) + " -saved to- " + str(sys.argv[2]) )
    #save argv[2] as key and what ever is in the clipboard as the value in the store file
    storeShelf[sys.argv[2]] = pyperclip.paste()

# if there are 2 arguments [0 and 1]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        #copy all the keys in the store file to the clipboad as a string
        pyperclip.copy(str(list(storeShelf.keys())))
        print(str(list(storeShelf.keys())) + " coppied to clipboard")
        #if argv[1] is in the store file
    elif sys.argv[1] in storeShelf:
        #look for the key and copy its value to the clipboard
        pyperclip.copy(storeShelf[sys.argv[1]])
        print(str(sys.argv[1]) + " value has been coppied to clipboard")

storeShelf.close()