import pyautogui
import webbrowser
webbrowser.open('http://www.google.com')
# searches for term  
pyautogui.sleep(3)          
pyautogui.press(['s','p','e','e','d','space','t','e','s','t'])
pyautogui.press(['enter'])
pyautogui.sleep(.5)
pyautogui.press(['tab'])
pyautogui.sleep(.5)
pyautogui.press(['tab'])
pyautogui.sleep(.5)
pyautogui.press(['tab'])
pyautogui.sleep(.5)
pyautogui.press(['tab'])
pyautogui.sleep(.5)
pyautogui.press(['tab'])
pyautogui.sleep(.5)
pyautogui.press(['tab'])
# this last enter should initiate the google test
pyautogui.press(['enter'])
# this should allow the test to run you may need to adjust the timer to be longer
pyautogui.sleep(30)
# the following will take the screenshot and save the file
im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('google_speedtest.png')
# this will quit the browser
with pyautogui.hold('command'):
        pyautogui.press(['q'])