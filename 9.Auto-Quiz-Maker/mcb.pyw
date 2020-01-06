#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve
import pyperclip
import sys

#open a shelve file named mcb and save it to mcbShelf
mcbShelf = shelve.open('mcb')

#if there are 3 arguments (0 to 2) and argv[1] is save
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    print(str(pyperclip.paste()) + " -saved to- " + str(sys.argv[2]) )
    #save argv[2] as key and what ever is in the clipboard as the value in the mcb file
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# if there are 2 arguments [0 and 1]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        #copy all the keys in the mcb file to the clipboad as a string
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.keys())) + " coppied to clipboard")
        #if argv[1] is in the mcb file
    elif sys.argv[1] in mcbShelf:
        #look for the key and copy its value to the clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(str(sys.argv[1]) + " value has been coppied to clipboard")

mcbShelf.close()