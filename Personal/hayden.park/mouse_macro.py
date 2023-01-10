import pyautogui as pag
import time

num = 0
try:
    while True:      
        pag.click(x=900,y=900)
        time.sleep(5)
        pag.click(x=910,y=910)
        time.sleep(5)
        num += 10
        print(num, "초 경과")

except KeyboardInterrupt:
    print("정지")

