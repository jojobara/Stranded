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
    gui.drag(W,H,duration=1.00)
    time.sleep(0.01)
    return       

def FinalCheck() :
    for i in range(len(c)-1):
        if len(c[i])!= len(c[i+1]) :
            print(c[i+1])
            print('LengthError')
            exit()
    return

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
for i in range(10) :
    for j in range(16) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*2 - 30
        H = ((pos[1].y- pos[0].y)/10)*1 - 30
        
        if int(c[i][j]) + int(c[i][j+1]) == 10 :
            
            drag(L, T, W, H)

            c[i] = c[i][:j] + '00' + c[i][j+2:]
            

for j in range(17) :
    for i in range(9) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*1 - 30
        H = ((pos[1].y- pos[0].y)/10)*2 - 30
        
        
        if int(c[i][j]) + int(c[i+1][j]) == 10 :

            drag(L, T, W, H)

            c[i]   = c[i][:j]   + '0' + c[i][j+1:]
            c[i+1] = c[i+1][:j] + '0' + c[i+1][j+1:]
            

for i in range(9) :
    for j in range(16) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*2 - 30
        H = ((pos[1].y- pos[0].y)/10)*2 - 30
        
        
        if int(c[i][j]) + int(c[i][j+1]) + int(c[i+1][j]) + int(c[i+1][j+1]) == 10 :

            drag(L, T, W, H)
            
            c[i]   = c[i][:j] +   '00' + c[i][j+2:]
            c[i+1] = c[i+1][:j] + '00' + c[i+1][j+2:]

for i in range(10) :
    for j in range(15) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*3 - 30
        H = ((pos[1].y- pos[0].y)/10)*1 - 30
        
        if int(c[i][j]) + int(c[i][j+1]) + int(c[i][j+2]) == 10 :

            drag(L, T, W, H)
            
            c[i] = c[i][:j] + '000' + c[i][j+3:]
            

for i in range(9) :
    for j in range(15) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*3 - 30
        H = ((pos[1].y- pos[0].y)/10)*2 - 30
        
        if int(c[i][j]) + int(c[i][j+1]) + int(c[i][j+2]) + int(c[i+1][j]) + int(c[i+1][j+1]) + int(c[i+1][j+2]) == 10 :

            drag(L, T, W, H)
            
            c[i]   = c[i][:j] +   '000' + c[i][j+3:]
            c[i+1] = c[i+1][:j] + '000' + c[i+1][j+3:]
            

for j in range(17) :
    for i in range(8) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*1 - 30
        H = ((pos[1].y- pos[0].y)/10)*3 - 30
        
        
        if int(c[i][j]) + int(c[i+1][j]) + int(c[i+2][j]) == 10 :

            drag(L, T, W, H)
            
            c[i]   = c[i][:j] +   '0' + c[i][j+1:]
            c[i+1] = c[i+1][:j] + '0' + c[i+1][j+1:]
            c[i+2] = c[i+2][:j] + '0' + c[i+2][j+1:]
            

for j in range(16) :
    for i in range(8) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*2 - 30
        H = ((pos[1].y- pos[0].y)/10)*3 - 30
        
        
        if int(c[i][j]) + int(c[i+1][j]) + int(c[i+2][j]) + int(c[i][j+1]) + int(c[i+1][j+1]) + int(c[i+2][j+1])== 10 :

            drag(L, T, W, H)
            
            c[i]   = c[i][:j]   + '00' + c[i][j+2:]
            c[i+1] = c[i+1][:j] + '00' + c[i+1][j+2:]
            c[i+2] = c[i+2][:j] + '00' + c[i+2][j+2:]
            

for i in range(8) :
    for j in range(15) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*3 - 30
        H = ((pos[1].y- pos[0].y)/10)*3 - 30
        
        
        if int(c[i][j]) + int(c[i][j+1]) + int(c[i][j+2]) + int(c[i+1][j]) + int(c[i+1][j+1]) + int(c[i+1][j+2])\
            + int(c[i+2][j]) + int(c[i+2][j+1]) +int(c[i+2][j+2]) == 10 :

            drag(L, T, W, H)
            
            c[i]   = c[i][:j]   + '000' + c[i][j+3:]
            c[i+1] = c[i+1][:j] + '000' + c[i+1][j+3:]
            c[i+2] = c[i+2][:j] + '000' + c[i+2][j+3:]
            

for i in range(10) :
    for j in range(14) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*4 - 30
        H = ((pos[1].y- pos[0].y)/10)*1 - 30
        
        if int(c[i][j]) + int(c[i][j+1]) + int(c[i][j+2]) + int(c[i][j+3]) == 10 :

            drag(L, T, W, H)
            
            c[i] = c[i][:j] + '0000' + c[i][j+4:]


for i in range(9) :
    for j in range(14) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*4 - 30
        H = ((pos[1].y- pos[0].y)/10)*2 - 30
        
        if int(c[i][j]) + int(c[i][j+1]) + int(c[i][j+2]) + int(c[i][j+3]) + int(c[i+1][j]) + int(c[i+1][j+1])\
            + int(c[i+1][j+2]) + int(c[i+1][j+3])== 10 :

            drag(L, T, W, H)
            
            c[i]   = c[i][:j]   + '0000' + c[i][j+4:]
            c[i+1] = c[i+1][:j] + '0000' + c[i+1][j+4:]


for i in range(8) :
    for j in range(14) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*4 - 30
        H = ((pos[1].y- pos[0].y)/10)*3 - 30
        
        if int(c[i][j]) + int(c[i][j+1]) + int(c[i][j+2]) + int(c[i][j+3]) + int(c[i+1][j]) + int(c[i+1][j+1])\
            + int(c[i+1][j+2]) + int(c[i+1][j+3]) + int(c[i+2][j]) + int(c[i+2][j+1]) + int(c[i+2][j+2]) + int(c[i+2][j+3])== 10 :

            drag(L, T, W, H)
            
            c[i]   = c[i][:j]   + '0000' + c[i][j+4:]
            c[i+1] = c[i+1][:j] + '0000' + c[i+1][j+4:]
            c[i+2] = c[i+2][:j] + '0000' + c[i+2][j+4:]


for j in range(17) :
    for i in range(7) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*1 - 30
        H = ((pos[1].y- pos[0].y)/10)*4 - 30
        
        
        if int(c[i][j]) + int(c[i+1][j]) + int(c[i+2][j]) + int(c[i+3][j]) == 10 :

            drag(L, T, W, H)
            
            c[i]   = c[i][:j]   + '0' + c[i][j+1:]
            c[i+1] = c[i+1][:j] + '0' + c[i+1][j+1:]
            c[i+2] = c[i+2][:j] + '0' + c[i+2][j+1:]
            c[i+3] = c[i+3][:j] + '0' + c[i+3][j+1:]


for j in range(16) :
    for i in range(7) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*2 - 30
        H = ((pos[1].y- pos[0].y)/10)*4 - 30
        
        
        if int(c[i][j]) + int(c[i+1][j]) + int(c[i+2][j]) + int(c[i+3][j]) + int(c[i][j+1]) + int(c[i+1][j+1])\
            + int(c[i+2][j+1]) + int(c[i+3][j+1])== 10 :

            drag(L, T, W, H)
            
            c[i]   = c[i][:j]   + '00' + c[i][j+2:]
            c[i+1] = c[i+1][:j] + '00' + c[i+1][j+2:]
            c[i+2] = c[i+2][:j] + '00' + c[i+2][j+2:]
            c[i+3] = c[i+3][:j] + '00' + c[i+3][j+2:]


for j in range(15) :
    for i in range(7) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*3 - 30
        H = ((pos[1].y- pos[0].y)/10)*4 - 30
        
        
        if int(c[i][j]) + int(c[i+1][j]) + int(c[i+2][j]) + int(c[i+3][j]) + int(c[i][j+1]) + int(c[i+1][j+1])\
            + int(c[i+2][j+1]) + int(c[i+3][j+1]) + int(c[i][j+2]) + int(c[i+1][j+2]) + int(c[i+2][j+2]) + int(c[i+3][j+2]) == 10 :
 
            drag(L, T, W, H)
            
            c[i]   = c[i][:j]   + '000' + c[i][j+3:]
            c[i+1] = c[i+1][:j] + '000' + c[i+1][j+3:]
            c[i+2] = c[i+2][:j] + '000' + c[i+2][j+3:]
            c[i+3] = c[i+3][:j] + '000' + c[i+3][j+3:]
  

for i in range(7) :
    for j in range(14) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*4 - 30
        H = ((pos[1].y- pos[0].y)/10)*4 - 30
        
        if int(c[i][j]) + int(c[i][j+1]) + int(c[i][j+2]) + int(c[i][j+3]) + int(c[i+1][j]) + int(c[i+1][j+1])\
            + int(c[i+1][j+2]) + int(c[i+1][j+3]) + int(c[i+2][j]) + int(c[i+2][j+1]) + int(c[i+2][j+2]) + int\
                (c[i+2][j+3]) + int(c[i+3][j]) + int(c[i+3][j+1]) + int(c[i+3][j+2]) + int(c[i+3][j+3])== 10 :
       
            drag(L, T, W, H)
            
            c[i]   = c[i][:j]   + '0000' + c[i][j+4:]
            c[i+1] = c[i+1][:j] + '0000' + c[i+1][j+4:]
            c[i+2] = c[i+2][:j] + '0000' + c[i+2][j+4:]
            c[i+3] = c[i+3][:j] + '0000' + c[i+3][j+4:]
        

for i in range(10) :
    for j in range(13) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*5 - 30
        H = ((pos[1].y- pos[0].y)/10)*1 - 30
        
        if int(c[i][j]) + int(c[i][j+1]) + int(c[i][j+2]) + int(c[i][j+3]) + int(c[i][j+4]) == 10 :
      
            drag(L, T, W, H)
            
            c[i] = c[i][:j] + '00000' + c[i][j+5:]
         

for j in range(17) :
    for i in range(6) :
        
        L = pos[0].x + (((pos[1].x-pos[0].x)/17)*j) +10
        T = pos[0].y + (((pos[1].y- pos[0].y)/10)*i) +10
        W = ((pos[1].x-pos[0].x)/17)*1 - 30
        H = ((pos[1].y- pos[0].y)/10)*5 - 30
        
        
        if int(c[i][j]) + int(c[i+1][j]) + int(c[i+2][j]) + int(c[i+3][j]) + int(c[i+4][j]) == 10 :
     
            drag(L, T, W, H)
            c[i]   = c[i][:j]   + '0' + c[i][j+1:]
            c[i+1] = c[i+1][:j] + '0' + c[i+1][j+1:]
            c[i+2] = c[i+2][:j] + '0' + c[i+2][j+1:]
            c[i+3] = c[i+3][:j] + '0' + c[i+3][j+1:]
            c[i+4] = c[i+4][:j] + '0' + c[i+4][j+1:]
   
print('---------------------------------')
print(c)