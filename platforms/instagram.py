# platforms/instagram.py
import pyautogui
import time
import pyperclip
from decision import classifier
from platforms.base import Platform

class InstagramPlatform(Platform):
    def __init__(self):
        super().__init__()
        self.name = "Instagram"
        self.shortcut = (1470, 730)
        self.reels_tab = (100, 560)
        self.like_button = (1741, 971)
        self.load_time = 5  # seconds to wait for page to load

    def click_shortcut(self):
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(self.load_time)

    def navigate_to_feed(self):
        pyautogui.moveTo(self.reels_tab)
        pyautogui.click()
        time.sleep(2)

    def scroll(self):
        pyautogui.scroll(-1)

    def like(self):
        pyautogui.moveTo(self.like_button)
        pyautogui.click()

    def extract_text(self) -> str:
        try:
            time.sleep(1)
            pyautogui.locateCenterOnScreen('images/instareels.png', region=(1680,950,100,500), confidence=0.8)
        except pyautogui.ImageNotFoundException:
            print("Image not found, resetting tab")
            self.close()
            self.setup()
        pyautogui.moveTo(1550, 1332)
        time.sleep(0.1)
        pyautogui.click() #more bar
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.click()
        pyperclip.copy("")   # clear clipboard explicitly
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
        time.sleep(0.2)
        pyautogui.click()
        pyautogui.moveTo(1750,950)
        time.sleep(0.1)
        clipboard = pyperclip.paste()
        text = clipboard.lower()
        return text

    def close(self):
        try:
            buttonnewtab = pyautogui.locateOnScreen('images/newtab.png', confidence=0.9)
            pyautogui.moveTo(buttonnewtab, duration=0)
            pyautogui.move(-60,0)
            time.sleep(1)
            pyautogui.click()
            time.sleep(2)
        except: 
            print("cant find delete")

    def update_like_button(self):
        try:
            button_like = pyautogui.locateCenterOnScreen('images/instalike.png', region=(1700, 1000, 100, 1000), confidence=0.8)
            if button_like:
                self.like_button = button_like
        except Exception as e:
            print(f"Error updating like button position: {e}")
            