Introduction:
This code uses the pyautogui python package to interact with social media reels (instagram and youtube) on a laptop. The purpose is to scroll through and like reels automatically to decrease the effectiveness of the algorithms on us. Currently for instagram certain words in the description decrease the probability of a like while other ones increase it. Meanwhile the youtube liking is completely random. This is partly to compare how the algorithm changes, and partly because instagram likes can be publicly seen so I wanted to minimise liking very weird reels for my social footprint. It makes your computer go into hibernation at the end so I leave it on when I go to bed and it runs for around 2 hours.

Scripts:
There are 2 scripts, main.py for all of the intended functionality (can run straight away but is designed to be compiled to executable code and run as a shortcut), and getcoords.py, designed to constantly return mouse coordinates so that it is easier to hardcode locations for the mouse to move to. I have another .ps1 script containing "Stop-Process -Name "Python" -Force -ErrorAction SilentlyContinue" which is bound to a shortcut to kill the script if needed

Packages:
Pyautogui, pyperclip, and pyinstaller

How to use:
To create a python executable run 'uv run pyinstaller main.py --onefile --noconsole' - this is using uv which I used for the project but if you are using pip I'm sure there's a way. Add the photos that are currently in the top folder to the folder with the .exe file. I then navigate to that executable in file explorer => right click drag to desktop => copy as shortcut => right click on it => properties => add whatever you want under the shortcut key. I'm not sure the button layout variability or difference in loading times between machines so they may need to be tuned, but what definitely does matter for the current code which has these positions hardcoded is being on a chrome browser with Instagram and Youtube as the 7th and 8th shortcuts respectively (followed only by the 'Add Shortcut' button). This could be changed to detect the images instead in future. 

Good luck, Ben