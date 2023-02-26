import pyautogui as pag
import time


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
  
  
def switchDesktop(next):
  if next:
    pag.hotkey('win', 'ctrl', 'right')
  else:
    pag.hotkey('win', 'ctrl', 'left')
    
    
  
  
  
# press('./Assets/vscode_readme.png')

# pag.screenshot('sc_shot.png')

# pag.typewrite('Hello world!\n', interval=0.2)

# press('./Assets/2.png')
# press('./Assets/1.png')

pag.PAUSE = 1
openApp('docker')
openApp('vis')

time.sleep(5)

switchDesktop(True)

openApp('slack')
openApp('obsidian')
openApp('chrome')
press('./Assets/chrome_candide.png')

# print(pag.size())


# print(pag.position())