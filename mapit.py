import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '200', 'elim nagar', 'perungudi']


#Check if commant line arguments were passed

if len(sys.argv) > 1:
    # ['mapit.py', '200', 'elim nagar', 'perungudi'] -> ' 200 elim nagar perungui'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

