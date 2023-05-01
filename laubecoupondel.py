import time

from PIL import ImageGrab
from functools import partial
import pyautogui
import pyperclip

#1858,220 #삭제
#1385,164 #확인


print(pyautogui.size())




# pyautogui.mouseInfo()
# print(pyautogui.size())
print(pyautogui.position())



n=11
for i in range(n):
    pyautogui.moveTo(1858,220)  # 쿠폰발행
    print(pyautogui.position())
    pyautogui.click(button='left')
    time.sleep(0.5)

    pyautogui.moveTo(1385,164)  # 쿠폰명
    print(pyautogui.position())
    pyautogui.click(clicks=2, button='left')
    time.sleep(1)

#
#


