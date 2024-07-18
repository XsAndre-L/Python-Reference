import pyautogui as pag


def openApp(appName):
    # pag.hotkey("alt", "space")
    pag.hotkey("win")
    pag.typewrite("." + appName, interval=0.05)
    pag.press("enter")


def switchDesktop(next):
    if next:
        pag.hotkey("win", "ctrl", "right")
    else:
        pag.hotkey("win", "ctrl", "left")
