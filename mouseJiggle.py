import pyautogui
import time 


def mouseJiggle():
    while True:
        time.sleep(3)
        pyautogui.move(0, 5, duration=0.05)
        time.sleep(3)
        pyautogui.move(0, -5, duration=0.05)

mouseJiggle()