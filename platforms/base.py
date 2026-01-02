# platforms/base.py
from abc import ABC, abstractmethod
import pyautogui
import time

class Platform(ABC):
    def __init__(self):
        self.good_count = 0
        self.bad_count = 0

    def open_new_tab(self):
        """Common logic for opening a new tab"""
        try:
            button_newtab = pyautogui.locateOnScreen('images/newtab.png', confidence=0.9)
            pyautogui.moveTo(button_newtab)
            pyautogui.click()
            time.sleep(0.2)

        except KeyboardInterrupt:
            print("Exiting due to user interrupt")
            raise  # stop recursion immediately

        except Exception as e:
            print(f"Error opening new tab: {e}")
            time.sleep(2)
            self.open_new_tab()  # Retry on failure
        
    @abstractmethod
    def click_shortcut(self):
        """Platform-specific shortcut click"""
        pass

    @abstractmethod
    def navigate_to_feed(self):
        """Go to Reels / Shorts / Feed"""
        pass

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def like(self):
        pass

    @abstractmethod
    def extract_text(self) -> str:
        pass

    @abstractmethod
    def close(self):
        pass

    def setup(self):
        """Shared setup sequence"""
        self.open_new_tab()
        self.click_shortcut()
        self.navigate_to_feed()
