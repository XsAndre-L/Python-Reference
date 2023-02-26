import pyautogui as pag


def press(imagePath):
  loc = pag.locateCenterOnScreen(imagePath, confidence=0.8)
  pag.moveTo(loc.x, loc.y, 1)
  pag.click(loc)
  
def dragTo():
  print('Drag')
  
def openApp(appName):
  pag.hotkey('alt', 'space')
  pag.typewrite('.'+appName, interval=0.05)
  pag.press('enter')
  
  
# press('./Assets/vscode_readme.png')

# pag.screenshot('sc_shot.png')

# pag.typewrite('Hello world!\n', interval=0.2)

# press('./Assets/2.png')
# press('./Assets/1.png')

openApp('vis')
openApp('docker')

# print(pag.size())


print(pag.position())