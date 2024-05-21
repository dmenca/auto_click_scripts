import pyautogui
import time

time.sleep(5)
while True:
    x, y = pyautogui.position()
    position_str = f"X: {x} Y: {y}"
    print(position_str, end="\n")
    time.sleep(1)