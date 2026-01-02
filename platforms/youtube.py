# platforms/youtube.py
import pyautogui
import time
import pyperclip
from platforms.base import Platform

class YouTubePlatform(Platform):
    def __init__(self):
        super().__init__()
        self.name = "YouTube"
        self.shortcut = (1620, 730)
        self.shorts_tab = (100, 330)
        self.like_button = (1700, 810)
        self.load_time = 15

    def click_shortcut(self):
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(self.load_time)

    def navigate_to_feed(self):
        pyautogui.moveTo(self.shorts_tab)
        pyautogui.click()
        time.sleep(2)

    def scroll(self):
        pyautogui.scroll(-1)

    def like(self):
        pyautogui.moveTo(self.like_button)
        pyautogui.click()

    def extract_text(self) -> str:
        pyperclip.copy("")
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.2)
        return pyperclip.paste().lower()

    def close(self):
        pyautogui.hotkey("ctrl", "w")
        time.sleep(2)

    def update_like_button(self):
        #do nothing
        pass