import pyautogui, sys
# use the display-mouse constant to see the mouse position and then use those numbers
pyautogui.moveTo(1585, 1000)   # moves mouse to X of 1585, Y of 1000.
# = = = = = = = = = =
# CLICKING
# pyautogui.click()  # click the mouse
# pyautogui.click(button='right')  # right-click the mouse
# pyautogui.doubleClick()  # perform a left-button double click
# ADDITIONAL FUNCTIONS
# pyautogui.moveTo(100, 200, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds
# pyautogui.moveTo(100, 200)  # moves mouse to X of 100, Y of 200.
# pyautogui.move(0, 50)       # move the mouse down 50 pixels.
# pyautogui.move(-30, 0)      # move the mouse left 30 pixels.
# pyautogui.move(-30, None)   # move the mouse left 30 pixels.
# = = = = = = = = = = 
# MOUSE DRAGGING
# pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
# pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
# pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button