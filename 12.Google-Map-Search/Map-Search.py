
import webbrowser
import sys
import pyperclip

# if there is a command line argument, assume that is the address
if len (sys.argv) > 1:
    address = ''.join(sys.argv[1])
    # else assume the address is saved the clipboard
else:
    address = pyperclip.paste()
# open google maps
webbrowser.open('www.google.com/maps/place/' + address)
