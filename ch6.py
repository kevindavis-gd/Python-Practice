
# this program stores passwords for different accounts. It copies the password of an account to the clipboard when the account name is written.
import sys, pyperclip
account = sys.argv[1] #this is the first command line argument


Passwords = {'email' : 'dshfjdhfjdshkjgdshjvndj', 
            'facebook' : 'jdhfkjdhfjkdshfkjsh', 
            'instagram' : 'kzdjbkjdfjkdsfjdhfj'}

if len(sys.argv) < 2:
    print('Usage: python ch6.py account')
    sys.exit()

if account in Passwords:
    pyperclip.copy(Passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('Password not in list, Please add password for' + account)
    newPassword = input()
    Passwords[account]= newPassword
    print("Password for " + account + " was added")

