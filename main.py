# main.py
import os
import pyautogui
import time
import random
import pyperclip
import ctypes

from platforms.instagram import InstagramPlatform
from platforms.youtube import YouTubePlatform
from decision.classifier import ContentClassifier
from engine.runner import Runner

AVG_WATCH_TIME_MINUTES = 30
LIKE_RATE = 0.1  # Base like rate, not added yet

good_count = 0
bad_count = 0
classifier = ContentClassifier()
# Get onto Insta Reels
def setup(app):
    try:
        buttonnewtab = pyautogui.locateOnScreen('images/newtab.png', confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("New tab button not found, retrying...")
        time.sleep(2)
        setup(app)
        return
    pyautogui.moveTo(buttonnewtab, duration=0)

    pyautogui.click()


    
    # Instagram Coordinate
    pyautogui.moveTo(app.shortcut) #Insta Shortcut
    sleep(1)
    pyautogui.click()
    sleep(app.load_time) #delays based on site loading time
    pyautogui.moveTo(app.reels_tab) #Reels Tab
    pyautogui.click()
    pyautogui.moveTo(app.like_button) #Like Button
    sleep(app.load_time)

def scroll_and_like(app):

    #Watch Time, approx chunks of half an hour
    watch_time = abs(random.randint(1,3) * AVG_WATCH_TIME_MINUTES * 30 + random.gauss(mu=0, sigma=500))
    print("Watchtime is: ", watch_time)
    counter = 0
    while counter < watch_time:
        if is_capslock_on():
            print("Capslock detected, taking a break...")
            time.sleep(2)
            continue
        #Watch Time
        randint = random.randint(-2,3)
        if randint < 0:
            randint = 0
        value = random.gauss(mu=4, sigma=(randint+1))  # mean 0, standard deviation 1
        delay = 4*randint + value
        if delay < 0:
            delay = delay * delay
        if delay < 1.5:
            delay = delay + 1.5
        if randint == 3:
            delay = delay + 7 + value
        
        #Time until potential like
        if app.name == "Instagram":
            text = app.extract_text()
            score = classifier.score(text)
            print("Content score: ", score)
        else:
            score = 1

        randint2 = random.randint(1,round(2+100/(delay*score))) #potential like
        delay2 = 0
        if randint2 == 1:
            delay2 = delay * random.gauss(mu=0.5, sigma=0.3)
            if delay2 < 0:
                delay2 = delay2 + delay

        #Random spike chance
        randint3 = random.randint(1,500)
        if randint3 == 50:
            delay = delay * random.gauss(mu=10, sigma=4)
            if delay < 0:
                delay = delay * delay
        counter = counter + delay
        print("Delay is: ", delay*score**(1/5))
        #print("Time until like is: ", delay2)
        sleep(delay2*score**(1/5))
        if delay2 > 0:
            if delay2 > delay:
                delay2 = delay - (random.gauss(mu=4, sigma=2))**2
            app.update_like_button()
            pyautogui.moveTo(app.like_button)
            pyautogui.click()
            print("Reel Liked")
        sleep((delay - delay2)*score**(1/5))
        pyautogui.scroll(-1)
    app.close()

def sleep(t):
    time.sleep(abs(t))

def is_capslock_on():
    # 0x14 is VK_CAPITAL
    return bool(ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1)

print(is_capslock_on())

def main():
    instagram = InstagramPlatform()
    youtube = YouTubePlatform()
    instagram.setup()
    #setup(instagram)
    scroll_and_like(instagram)

    setup(youtube)
    scroll_and_like(youtube)
    os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
if __name__ == "__main__":
    main()

