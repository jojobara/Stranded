
import pyautogui as gui
import time
import keyboard

a = '6739225 59779429 8 1'
print(a)
print(type(a))

a = a.replace('6','six')
print(a)

b = ['1', '23', '456', '789123']
print(len(b))
print(b[0])

def LenCheck(x):
    if len(b[x])==3 :
        return b[x]

for i in range(len(b)):
    if LenCheck(i)!=None :
        print(LenCheck(i))

str1 = '441'
print(str1[0])
print(str1[2])
new_str = str1[0]+str1[2]
print(new_str)
print(type(str1))

def ManualCheck (str1) :
    for i in range(len(c)):
        if len(c[i])!=17 :
            print(c[i])
            str2 = str1[0]+str1[2]
            c[i] = c[i].replace(str1,str2)
    return

c =['14896835421151378', '17432114187863517', '82129828579252962', '67756317135973943', '14214711389151881', '25836122971558264', '67351893429459386', '46123387359436954', '21535298994929638', '26962144127762563']

print(len(c))
ManualCheck('465')

print('///////////////////////////')

for i in range(10) :
    if len(c[i]) != 17 :
        print(c[i])

print(c)

d = 'hello'
print(c[1])
#c[i] = c[i][:j] + 'f' + c[i][j+1:]
print(c[1])

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

pos = get_positions()

def drag(L,T,W,H) :
    gui.moveTo(L,T)
    gui.drag(W,H,duration=1.00)
    time.sleep(0.01)
    return     



def IsitTen (x,y) :
    
    Z = ''
    for i in range(x) :
        Z += '0'
    
    print(Z)
    print(type(Z))
    
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
                print(X)
            
                if sum(X) == 10 :
                    print('IFoundit')
                    print(c[i][j])
                    print(i)
                    print(j)
               
                    drag(L, T, W, H)
                    
                    for m in range(y) :
                        c[i+m] = c[i][:j] + Z + c[i][j+x]
    return c
                
                
IsitTen(3, 2)
