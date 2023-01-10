import os
os.system('clear')
from support import runcmd
try:
    import pyfiglet
except:
    os.system('pip install pyfiglet')

import pyfiglet

R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"

fig = pyfiglet.figlet_format("CodeAx1")
print(B+fig)

print(G+'''
[ Website clone make Easy ]
Coded By CodeAx1
_________________________________________________''')

print(B+"               CodeAx1             ")
print()
print()
while True:
    websitename = input(R+"Enter Website Name: ")
    try:
        print('Your Given Website is : '+websitename)
        webreal = input('Press Yes or No: ')
        if webreal.lower() == 'yes':
            print("Hey We Are Cloning Your Given Website")
            print(G+"Please wait 10sec...")
            runcmd("wget --random-wait -r -p robots=off -U mozilla "+websitename,verbose = True)
            print()
            print('We Have Finally Cloned And Saved a copy on this folder :')
            print('Successfully Exit')
            print()
            print()
            print(Y+' For Quitting Press CLTR + C')
        else:
            print('Okay We Are Running Again')
            break
    except:
        print(B'Something went Wrong...')
        print(B'Contact CodeAx1...on instagram')
