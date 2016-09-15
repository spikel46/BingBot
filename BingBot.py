#Joseph Koblitz
#Version 1.5
#Built for Python 3.5.2


import os, sys, shutil
import pyautogui #gives all our automation functionality
import webbrowser #https://docs.python.org/3/library/webbrowser.html

pyautogui.PAUSE = 1 #pause between each pyautogui func call
pyautogui.FAILSAFE = True #move mouse cursor to the upper-left corner


NUM_BROWSERS = 4
BROWSER_RANGE = NUM_BROWSERS + 1
CHOICE_ARG = 1
ENTER = "enter" #just the enter key

#browsers I have added functionality for
browsers = ["Firefox", "Chrome", "Safari", "Default Browser"]

#put topics you won't get tired of in this list
searches = ["top stories","seattle hackathons","futuristic tech","russian classes seattle",
"sbux stock","tmus stock","msft stock","how many days until january 3rd","elon musk",
"kendrick jcole collab","is bleach manga over", "GRE Exam tips","daydream vr",
"hololens","how to make your own web browser", "Rick and Morty Season 3", "Galaxy Note 7"]

#menu for people
def menu():
	print("Hi! Welcome to my program which is essentially meant to automatically get you free Microsoft Rewards.",
		"\nDo you have a preferred web browser?")
	for i in range(0,NUM_BROWSERS):
		print(i+1,":",browsers[i])

	choice = 0
	while choice not in range(1, BROWSER_RANGE):
		choice = int(input("Please enter your choice ({} for quit): ".format(BROWSER_RANGE)))
		if choice == BROWSER_RANGE:
			exit()
	return choice

#creates a new tab
def newtab():
	pyautogui.keyDown("ctrlleft")
	pyautogui.press("t")
	pyautogui.keyUp("ctrlleft")

if(len(sys.argv) > 2):
	print("Invalid argument number, please try again")
	exit()
elif(len(sys.argv) ==1):
	choice = menu()
else:
	choice = int(sys.argv[CHOICE_ARG])
	if choice not in range (1, NUM_BROWSERS):
		print("Sorry, your input was not valid. Redirecting to menu...\n\n\n")
		choice = menu()


if shutil.which(browsers[choice-1]) == None:
	print("Python can't find your browser, please consult README")
	exit()

if(choice == 4):
	browser = webbrowser.get()
else:
	browser = webbrowser.get(browsers[choice-1].lower())

browser.open_new("https://www.bing.com")

"""
for i in range(21):
	if i in range(len(searches)):
		pyautogui.typewrite(searches[i])
	else:
		pyautogui.typewrite(str(i))
	pyautogui.press(ENTER)
	if(i != 20):
		newtab()
"""
