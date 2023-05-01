import time

from PIL import ImageGrab
from functools import partial
import pyautogui
import pyperclip



#화면배율 75%
print(pyautogui.size())




# pyautogui.mouseInfo()
# print(pyautogui.size())
print(pyautogui.position())
couponname =["김재헌님을 위한 쿠폰1",
"전세은님을 위한 쿠폰1",
"장재혁님을 위한 쿠폰1",
"박유진님을 위한 쿠폰1",
"태유빈님을 위한 쿠폰1",
"황정현님을 위한 쿠폰1",
"김예빈님을 위한 쿠폰1",
"안준영님을 위한 쿠폰1",
"박진우님을 위한 쿠폰1",
"박수정님을 위한 쿠폰1",
"이은효님을 위한 쿠폰1",
"김주상님을 위한 쿠폰1",
"황찬현님을 위한 쿠폰1",
"이예림님을 위한 쿠폰1",
"김재헌님을 위한 쿠폰2",
"전세은님을 위한 쿠폰2",
"장재혁님을 위한 쿠폰2",
"박유진님을 위한 쿠폰2",
"태유빈님을 위한 쿠폰2",
"황정현님을 위한 쿠폰2",
"김예빈님을 위한 쿠폰2",
"안준영님을 위한 쿠폰2",
"박진우님을 위한 쿠폰2",
"박수정님을 위한 쿠폰2",
"이은효님을 위한 쿠폰2",
"김주상님을 위한 쿠폰2",
"황찬현님을 위한 쿠폰2",
"이예림님을 위한 쿠폰2",
"김재헌님을 위한 쿠폰3",
"전세은님을 위한 쿠폰3",
"장재혁님을 위한 쿠폰3",
"박유진님을 위한 쿠폰3",
"태유빈님을 위한 쿠폰3",
"황정현님을 위한 쿠폰3",
"김예빈님을 위한 쿠폰3",
"안준영님을 위한 쿠폰3",
"박진우님을 위한 쿠폰3",
"박수정님을 위한 쿠폰3",
"이은효님을 위한 쿠폰3",
"김주상님을 위한 쿠폰3",
"황찬현님을 위한 쿠폰3",
"이예림님을 위한 쿠폰3",





]
couponcode =[
"kjh1",
"jse1",
"jjh1",
"pyj",
"tyb1",
"hjh1",
"kyb1",
"ajy1",
"pjw1",
"psj1",
"leh1",
"kjs1",
"hch1",
"lyl1",
"kjh2",
"jse2",
"jjh2",
"pyj",
"tyb2",
"hjh2",
"kyb2",
"ajy2",
"pjw2",
"psj2",
"leh2",
"kjs2",
"hch2",
"lyl2",
"kjh3",
"jse3",
"jjh3",
"pyj",
"tyb3",
"hjh3",
"kyb3",
"ajy3",
"pjw3",
"psj3",
"leh3",
"kjs3",
"hch3",
"lyl3",






]

discountrate = 100 #할인율
volume = 1 # 쿠폰개수

maxprice = 41600 # 최대금액설정


n= 42

for i in range(n):
    pyautogui.moveTo(1380, 657)  # 쿠폰발행
    print(pyautogui.position())
    pyautogui.click(button='left')

    pyautogui.moveTo(1242, 557)  # 쿠폰명
    print(pyautogui.position())
    pyautogui.click(button='left')
    pyperclip.copy(couponname[i])
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.moveTo(1233, 594)  # 쿠폰코드
    print(pyautogui.position())
    pyautogui.click(button='left')
    pyperclip.copy(couponcode[i])
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.moveTo(1293, 635)  # 할인 %
    print(pyautogui.position())
    pyautogui.click(button='left')

    pyautogui.moveTo(1211, 676)  # 할인금액(율)
    print(pyautogui.position())
    pyautogui.click(button='left')
    pyperclip.copy(discountrate)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.moveTo(1218, 719)  # 전체발행수
    print(pyautogui.position())
    pyautogui.click(button='left')
    pyperclip.copy(volume)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.moveTo(1219, 800)  # 최대금액설정
    print(pyautogui.position())
    pyautogui.click(button='left')
    pyperclip.copy(maxprice)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.moveTo(1222, 924)  # 사용
    print(pyautogui.position())
    pyautogui.click(button='left')

    pyautogui.moveTo(1335, 967)  # 등록
    print(pyautogui.position())
    pyautogui.click(button='left')
    time.sleep(2)

# for i in range(100):
#     pyautogui.scroll(-5000)

