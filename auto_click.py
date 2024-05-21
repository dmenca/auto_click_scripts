import pyautogui
import time
from datetime import datetime

# 通过坐标列表、间隔时间来进行点击
def click_by_pos_list(pos_list: list, interval_second: int):
    for (x, y) in pos_list:
        # 移动到指定坐标并点击
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        print(f"Clicked on ({x}, {y}),current time:{time_str}")
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval_second)
# 暂停秒以便切换到目标窗口
time.sleep(5)
# 点击事件的间隔事件
interval_second = 20
# 点击按钮的坐标列表, 也就是claim的坐标列表
pos_list = [(-1641, 374), (-1165, 395), (-606, 450)]
while True:
    click_by_pos_list(pos_list, interval_second)
    # 每隔30s重新点击一次怕失败了 一直循环调用 如果claim消失了也可以不点击
    time.sleep(30)
