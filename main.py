import pyautogui  # to control mouse and keyboard package
import time
pyautogui.FAILSAFE = False
while True:
    time.sleep(10)
    for i in range(0, 200):
        pyautogui.moveTo(0, i * 5)
    for i in range(0, 3):
        pyautogui.press('shift')