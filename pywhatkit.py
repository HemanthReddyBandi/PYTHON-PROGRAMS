import pyautogui
import time
time.sleep(7)
count=0
while count<=2:
    pyautogui.typewrite("ekkada vunnav")
    pyautogui.press ("enter")
    
    # for linkedin send button
    #pyautogui.hotkey("ctrl", "enter") 
    count=count+1