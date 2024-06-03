import pyautogui
import time
import threading
import keyboard

class AutoClicker:
    def __init__(self, interval):
        self.interval = interval
        self.running = False
        self.thread = None
        self.position = None

    def set_position(self):
        self.position = pyautogui.position()
        print(f"Position set to {self.position}.")

    def start_clicking(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.click)
            self.thread.start()
            print(f"Auto-clicker started at position {self.position}.")
        else:
            print("Auto-clicker is already running.")

    def stop_clicking(self):
        if self.running:
            self.running = False
            self.thread.join()
            print("Auto-clicker stopped.")
        else:
            print("Auto-clicker is not running.")

    def click(self):
        while self.running:
            pyautogui.click(self.position)
            time.sleep(self.interval)

def main():
    interval = float(input("Enter the interval between clicks in seconds: "))

    clickers = {
        'browser1': AutoClicker(interval),
        'browser2': AutoClicker(interval),
        'browser3': AutoClicker(interval)
    }

    print("Press 'Ctrl+1' to set position, start and stop auto-clicker for Browser 1.")
    print("Press 'Ctrl+2' to set position, start and stop auto-clicker for Browser 2.")
    print("Press 'Ctrl+3' to set position, start and stop auto-clicker for Browser 3.")

    def handle_clicker(browser_key):
        clicker = clickers[browser_key]
        if clicker.position is None:
            clicker.set_position()
        elif clicker.running:
            clicker.stop_clicking()
        else:
            clicker.start_clicking()

    keyboard.add_hotkey('ctrl+1', handle_clicker, args=('browser1',))
    keyboard.add_hotkey('ctrl+2', handle_clicker, args=('browser2',))
    keyboard.add_hotkey('ctrl+3', handle_clicker, args=('browser3',))

    # Keep the script running
    keyboard.wait('esc')

if __name__ == "__main__":
    main()