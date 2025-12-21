import pyautogui
import time
import random
import os

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
        randint2 = random.randint(1,round(1+100/delay))
        delay2 = 0
        if randint2 == 2:
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
        print("Delay is: ", delay)
        print("Time until like is: ", delay2)
        time.sleep(delay2)
        if delay2 > 0:
            if delay2 > delay:
                delay2 = delay - (random.gauss(mu=4, sigma=2))**2
            pyautogui.click()
            print("Reel Liked")
        time.sleep(delay - delay2)
        pyautogui.scroll(-1)

    print("Finished watching, closing tab")
    newtabadd = pyautogui.locateOnScreen('newtab.png', confidence=0.9)
    pyautogui.moveTo(newtabadd, duration=0)
    pyautogui.move(-60,0)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

def main():
    time.sleep(3)
    buttonnewtab = pyautogui.locateOnScreen('newtab.png', confidence=0.9)
    insta = [1620,730], [100,560], [1750,950], [5,5] #shortcut, reels tab, like button, load times
    yt = [1770,730], [100,330], [1700,810], [15,5]

    setup(insta, buttonnewtab)
    scroll_and_like(insta, buttonnewtab)

    setup(yt, buttonnewtab)
    scroll_and_like(yt, buttonnewtab)
    #Need to add close tab function
    os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
if __name__ == "__main__":
    main()

