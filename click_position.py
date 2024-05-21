import pyautogui
import time

time.sleep(5)
x, y = pyautogui.position()
position_str = f"X: {x} Y: {y}"
print(position_str, end="")