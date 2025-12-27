import pyautogui
import time
import random
import os
import pyperclip

# Get onto Insta Reels
def setup(app, buttonnewtab):
    pyautogui.moveTo(buttonnewtab, duration=0)
    pyautogui.click()

    # Instagram Coordinate
    pyautogui.moveTo(app[0][0], app[0][1], duration=0) #Insta Shortcut
    time.sleep(1)
    pyautogui.click()
    time.sleep(app[3][0]) #delays based on site loading time
    pyautogui.moveTo(app[1][0], app[1][1], duration=0) #Reels Tab
    pyautogui.click()
    pyautogui.moveTo(app[2][0], app[2][1], duration=0) #Like Button
    time.sleep(app[3][1])

def scroll_and_like(app, buttonnewtab):
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
        hashtags = search_hashtags(app, buttonnewtab) if app[0][0] == 1470 else 1
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
        time.sleep(delay2)
        if delay2 > 0:
            if delay2 > delay:
                delay2 = delay - (random.gauss(mu=4, sigma=2))**2
            pyautogui.click()
            print("Reel Liked")
        time.sleep(delay - delay2)
        pyautogui.scroll(-1)

    close_tab()

def search_hashtags(insta, buttonnewtab): #making just for insta at the moment
    try:
        pyautogui.locateCenterOnScreen('instareels.png', region=(1680,950,100,500), confidence=0.8)
    except pyautogui.ImageNotFoundException:
        print("Image not found, resetting tab")
        close_tab()
        setup(insta, buttonnewtab)
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
    text = clipboard
    #print("Clipboard contents:", extract_captions(text))
    badwords = ["gym", "self", "fitness", "fashion", "movie", "film", "america", "politics", "food", "game", "philosophy", "trump", "hot", "girl", "tate", "redpill", "kirk"]
    # If text can be a list of strings, join first
    if isinstance(text, list):
        text = "\n".join(text)
    text = text.lower()
    badwords = [w.lower() for w in badwords]

    if any(w in text for w in badwords):
        print("Bad match found:    ", text)
        return 0.1

    words = ["math", "physics" , "sewing", "knitting", "crochet", "christianity", "christian", "python", "coding", "programming", "developer", "software", "engineer", "quant", "investing"]
    # If text can be a list of strings, join first
    if isinstance(text, list):
        text = "\n".join(text)
    text = text.lower()
    words = [w.lower() for w in words]

    if any(w in text for w in words):
        print("Match found:    ", text)
        return 4

    return 1 
    
def close_tab():
    print("Finished watching, closing tab")
    try:
        newtabadd = pyautogui.locateOnScreen('newtab.png', confidence=0.9)
        pyautogui.moveTo(newtabadd, duration=0)
        pyautogui.move(-60,0)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
    except: 
        print("cant find delete")

def main():
    time.sleep(3)
    buttonnewtab = pyautogui.locateOnScreen('newtab.png', confidence=0.9)
    insta = [1470,730], [100,560], [1741,971], [5,5] #shortcut, reels tab, like button, load times
    yt = [1620,730], [100,330], [1700,810], [15,5]

    setup(insta, buttonnewtab)
    scroll_and_like(insta, buttonnewtab)

    setup(yt, buttonnewtab)
    scroll_and_like(yt, buttonnewtab)
    os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
if __name__ == "__main__":
    main()

