import pyautogui
import time
import random
import os
import pyperclip

# Get onto Insta Reels
def setup(app):
    try:
        buttonnewtab = pyautogui.locateOnScreen('newtab.png', confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("New tab button not found, retrying...")
        time.sleep(2)
        setup(app)
        return
    pyautogui.moveTo(buttonnewtab, duration=0)

    pyautogui.click()

    # Instagram Coordinate
    pyautogui.moveTo(app[0][0], app[0][1], duration=0) #Insta Shortcut
    sleep(1)
    pyautogui.click()
    sleep(app[3][0]) #delays based on site loading time
    pyautogui.moveTo(app[1][0], app[1][1], duration=0) #Reels Tab
    pyautogui.click()
    pyautogui.moveTo(app[2][0], app[2][1], duration=0) #Like Button
    sleep(app[3][1])

def scroll_and_like(app):
    #Watch Time, approx chunks of half an hour
    watch_time = random.randint(1,3) * 1469 + random.gauss(mu=0, sigma=500)
    print("Watchtime is: ", watch_time)
    counter = 0
    while counter < watch_time:
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
        hashtags = search_hashtags(app) if app[0][0] == 1470 else 1
        randint2 = random.randint(1,round(2+100/(delay*hashtags))) #potential like
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
        #print("Delay is: ", delay)
        #print("Time until like is: ", delay2)
        sleep(delay2)
        if delay2 > 0:
            if delay2 > delay:
                delay2 = delay - (random.gauss(mu=4, sigma=2))**2
            pyautogui.click()
            print("Reel Liked")
        sleep(delay - delay2)
        pyautogui.scroll(-1)

    close_tab()

def search_hashtags(insta): #making just for insta at the moment
    try:
        pyautogui.locateCenterOnScreen('instareels.png', region=(1680,950,100,500), confidence=0.8)
    except pyautogui.ImageNotFoundException:
        print("Image not found, resetting tab")
        close_tab()
        setup(insta)
    pyautogui.moveTo(1550, 1332)
    sleep(0.1)
    pyautogui.click() #more bar
    sleep(0.3)
    pyautogui.click()
    sleep(0.3)
    pyautogui.click()
    pyperclip.copy("")   # clear clipboard explicitly
    sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
    sleep(0.2)
    pyautogui.click()
    pyautogui.moveTo(1750,950)
    sleep(0.1)
    clipboard = pyperclip.paste()
    text = clipboard
    #print("Clipboard contents:", extract_captions(text))
    badwords = [] #fill in your own words to avoid
    # If text can be a list of strings, join first
    if isinstance(text, list):
        text = "\n".join(text)
    text = text.lower()
    badwords = [w.lower() for w in badwords]

    if any(w in text for w in badwords):
        print("Bad match found:    ", text)
        return 0.01

    words = [] #fill in your own words to like
    # If text can be a list of strings, join first
    if isinstance(text, list):
        text = "\n".join(text)
    text = text.lower()
    words = [w.lower() for w in words]

    if any(w in text for w in words):
        print("Match found:    ", text)
        return 1000

    return 1 
    
def close_tab():
    print("Finished watching, closing tab")
    try:
        newtabadd = pyautogui.locateOnScreen('newtab.png', confidence=0.9)
        pyautogui.moveTo(newtabadd, duration=0)
        pyautogui.move(-60,0)
        sleep(1)
        pyautogui.click()
        sleep(2)
    except: 
        print("cant find delete")

def sleep(t):
    time.sleep(abs(t))

def main():
    insta = [1470,730], [100,560], [1741,971], [5,5] #shortcut, reels tab, like button, load times
    yt = [1620,730], [100,330], [1700,810], [15,5]

    setup(insta)
    scroll_and_like(insta)

    setup(yt)
    scroll_and_like(yt)
    os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
if __name__ == "__main__":
    main()

