import os
import pyautogui
import time


file = os.startfile('F:\Skype')
time.sleep(2)
pyautogui.click(610,372)
pyautogui.typewrite('your id')
pyautogui.press('enter')
time.sleep(7)
pyautogui.typewrite('your password')
pyautogui.press('enter')
