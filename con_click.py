import threading
import time
import keyboard

import pyautogui


class AutoClick:
    def __init__(self, interval):
        self.interval = interval
        self.running = False
        self.thread = None

    def start_clicking(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.click)
            self.thread.start()
            print("Auto-clicker started")
        else:
            print("Auto-clicker is already running")

    def stop_clicking(self):
        if self.running:
            self.running = False
            print("Auto-clicker stopped")
        else:
            print("Auto-clicker is not running")

    def click(self):
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)


def main():
    interval = float(input("Enter the interval between clicks in seconds."))
    clicker = AutoClick(interval)
    print("Press 'F1' to start and stop the auto-clicker.")
    while True:
        keyboard.wait('F1')
        if clicker.running:
            clicker.stop_clicking()
        else:
            clicker.start_clicking()


if __name__ == "__main__":
    main()
