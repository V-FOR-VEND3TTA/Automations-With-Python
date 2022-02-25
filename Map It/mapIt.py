# This program launches a map in the browser using an address from the cmd or clipboard

# 1. Figure out the URL
# Formatted like this https://google.com/maps/places/address

# 2. Handle the command line arguments
import webbrowser, sys
import pyperclip


if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
# 3. Handle the clipboard content and launch the browser    
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
