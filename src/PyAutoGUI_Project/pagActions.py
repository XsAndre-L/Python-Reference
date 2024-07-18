import pyautogui as pag


def press(imagePath):
    loc = pag.locateCenterOnScreen(imagePath, confidence=0.8)
    pag.moveTo(loc.x, loc.y, 1)
    pag.click(loc)


def dragTo():
    print("Drag")
