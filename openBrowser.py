# this script will open a browser and type the word 'test' (note that the sleep timer may need to be adjusted depending on machine speed)
import pyautogui
import webbrowser
webbrowser.open('http://www.google.com')
# searches for term  
pyautogui.sleep(2)          
pyautogui.press(['t','e','s','t'])
pyautogui.press(['enter'])