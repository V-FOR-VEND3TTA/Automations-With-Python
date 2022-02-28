# This program launches Google in the browser using text from the cmd or clipboard

# 1. Figure out the URL
# The website I want to go on is formatted like this https://google.com/search?q=

# 2. Handle the command line arguments
import webbrowser, sys
import pyperclip


if len(sys.argv) > 1:
    # Get address from command line
    query = ' '.join(sys.argv[1:])
# 3. Handle the clipboard content and launch the browser    
else:
    query = pyperclip.paste()

webbrowser.open('https://www.google.com/search?q=' + query)
