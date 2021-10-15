import pyautogui
import webbrowser
webbrowser.open('http://www.google.com')
# opens search
with pyautogui.hold('command'):
        pyautogui.press(['space'])
# searches for term            
pyautogui.press(['t','e','r','m'])
# hits enter to open terminal
pyautogui.press(['enter'])

# the rest of this script will likely need sleep commands on it to function
# starts firefox profile script
# pyautogui.press(['.','/','f','i','r','e','f'])
# hits tab to autocomplete
# pyautogui.press(['tab'])
# hits enter to firefox profiles
# pyautogui.press(['enter'])