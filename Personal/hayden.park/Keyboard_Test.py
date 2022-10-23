import keyboard
import time
# ↑ : 72 / ↓ : 80 / → : 77 / ← : 75
running = True
while running:
    if keyboard.is_pressed(80):
        print('아래쪽 방향키 입력')
        time.sleep(0.1)
    elif keyboard.is_pressed(72):
        print('위쪽 방향키 입력')
        time.sleep(0.1)
    elif keyboard.is_pressed(77):
        print('오른쪽 방향키 입력')
        time.sleep(0.1)
    elif keyboard.is_pressed(75):
        print('왼쪽 방향키 입력')
        time.sleep(0.1)
    elif keyboard.is_pressed("q"):
        print('프로그램 종료')
        running = False


