import cv2
import pytesseract
import pyautogui as gui
import time
import keyboard

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

traineddata='lemon'

def get_positions():
    locations = []
    while 1:
        if keyboard.is_pressed('a'):
            pos = gui.position()
            print(pos)
            locations.append(pos)
            time.sleep(0.5)
        if keyboard.is_pressed('d'):
            print('stop record coordinate')
            return locations

def drag(L,T,W,H) :
    gui.moveTo(L,T)
    gui.drag(W,H,duration=0.90)
    time.sleep(0.01)
    return       

def FinalCheck() :
    for i in range(len(c)-1):
        if len(c[i])!= len(c[i+1]) :
            print(c[i+1])
            print('LengthError')
            exit()
    return

def IsitTen (x,y) :
    
    Z = ''
    for i in range(x) :
        Z += '0'
    
    
    for i in range(11-y) :
        
        for j in range(18-x) :
            
            X = []
            
            for k in range(x) :
                for l in range(y) :                    
                    X.append(int(c[i+l][j+k]))
                    
            
            
            L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
            T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
            W = ((pos[1].x-pos[0].x)/17)*x - 30
            H = ((pos[1].y- pos[0].y)/10)*y - 30
            
            if len(X) == x*y :
            
                if sum(X) == 10 :
                    #print('IFoundit')
               
                    drag(L, T, W, H)
                    
                    for m in range(y) :
                    
                        c[i+m] = c[i+m][:j] + Z + c[i+m][j+x:]
                        
                    X = []
    return c

filepath = 'C:\Pysp\Apple\Test.png'
pos = get_positions()
#gui.screenshot(filepath, region = (1180, 510, 610, 355))
gui.screenshot(filepath, region = (pos[0].x, pos[0].y, pos[1].x-pos[0].x, pos[1].y- pos[0].y))
a = cv2.imread(filepath)
b = cv2.inRange(a, (29, 76, 29), (31, 78, 31))
cv2.imwrite(filepath,255-b)
c = pytesseract.image_to_string(filepath,lang='lemon', config='--psm 6')


c = c.replace(' ','')

c = c.splitlines()

print('---------------------------------')
print(c)

print('---------------------------------')
FinalCheck()

print('---------------------------------')

for y in range(10) :
    for x in range(17) :
        IsitTen(x, y)

for x in range(17) :
    for y in range(10) :
        IsitTen(x, y)