# INSTALL MODULES:
# pip install schedule
# pip install pyautogui

import schedule, pyautogui, sys, time

def move_mouse():
    print("Keep pressing CTRL+C to stop program")
    pyautogui.moveTo(100,100,1)
    pyautogui.moveTo(100,400,1)
    pyautogui.moveTo(250,400,1)

schedule.every(5).minutes.do(move_mouse)
while True:
    schedule.run_pending()
    time.sleep(1)