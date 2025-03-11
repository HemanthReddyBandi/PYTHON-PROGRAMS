import pyautogui
import time
import webbrowser
time.sleep(6)
webbrowser.open("web.whatsapp.com")
for i in range(1000):
    pyautogui.typewrite("heheh....")
    pyautogui.press("enter")