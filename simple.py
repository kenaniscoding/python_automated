import pyautogui, os, time, sys
# MOUSE CONTROL
# Get current mouse position
duration = 1
def method1_try_except():
    """Exit loop with Ctrl+C using try-except"""
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Current mouse position: ({x}, {y})")
            time.sleep(0.1)  # Small delay to prevent spam
    except KeyboardInterrupt:
        print("\nExiting... Ctrl+C pressed")
        sys.exit(0)
def set_trimester(title, isChild, arrowDown):
    # reset to position
    pyautogui.moveTo(1952, 697)
    pyautogui.scroll(1000)
    # click add
    pyautogui.click(2266, 725)
    time.sleep(duration)
    # click add category
    pyautogui.press('down', 2)
    pyautogui.press('enter')
    time.sleep(duration+1)
    # click title textbox
    # pyautogui.click(1411, 508)
    pyautogui.press('tab')
    time.sleep(duration)
    pyautogui.press('tab')
    time.sleep(duration)
    # put title text
    pyautogui.write(title)
    time.sleep(duration+1)
    pyautogui.scroll(-1000)
    if (isChild):
        # click parent category 
        time.sleep(duration)
        pyautogui.click(1479,1052)
        time.sleep(duration)
        pyautogui.press('down', presses=arrowDown)  # Press 5 times quickly
        # press down arrow by n. arrowDown times
        pyautogui.press('enter')
    time.sleep(duration)
    pyautogui.click(2440,1282)
    time.sleep(duration+2)
    # click continue when recalculating grades
    pyautogui.click(1930, 843)
    time.sleep(duration+3)
# 690 x 630
# MOBILE MODE (ctrl + shift + i)
os.system('cls')
print("DO NOT TOUCH YOUR PC")
# method1_try_except()
# set_trimester("1st Trimester", False, 0)
# set_trimester("2nd Trimester", False, 0)
# set_trimester("3rd Trimester", False, 0)
# print("PARENTS DONE")
# set_trimester("1st Trimester Written Works", True, 1)
# set_trimester("1st Trimester Performance Tasks", True, 1)
set_trimester("2nd Trimester Written Works", True, 2)
set_trimester("2nd Trimester Performance Tasks", True, 2)
set_trimester("3rd Trimester Written Works", True, 3)
set_trimester("3rd Trimester Performance Tasks", True, 3)
os.system('cls')
print("DONE")
