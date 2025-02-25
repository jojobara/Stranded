import pyautogui as gui
import keyboard
import time

def screen_catch(img,region,confidence=0.975):
    for i in range(3) :
        pos = gui.locateOnScreen(img,confidence=confidence,region=region)
        time.sleep(0.001)
        if pos != None:
            return pos
    if pos == None:
        return
    
    
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

def drag(box) :
    gui.moveTo(box.left,box.top)
    gui.drag(box.width+10,box.height+10,duration=0.50)
    time.sleep(0.01)
    return

try:
    img = './37.png'
    pos = get_positions()
    region = (pos[0].x, pos[0].y, pos[1].x-pos[0].x, pos[1].y- pos[0].y)
    while 1:
       loc = screen_catch(img,region)
       drag(loc)
       gui.moveTo(100,100)
        
       if keyboard.is_pressed('s'):
           print('stop')
           break
except gui.ImageNotFoundException:
    
    try:    
        print('91')
        img = './91.png'
        while 1:
            loc = screen_catch(img,region)
            drag(loc)
            gui.moveTo(100,100)
        
            if keyboard.is_pressed('s'):
                print('stop')
                break
            
    except gui.ImageNotFoundException:
        try:    
            print('28')
            img = './28.png'
            while 1:
                loc = screen_catch(img,region)
                drag(loc)
                gui.moveTo(100,100)
            
                if keyboard.is_pressed('s'):
                    print('stop')
                    break
                
        except gui.ImageNotFoundException:
            
            try:    
                print('73')
                img = './73.png'
                while 1:
                    loc = screen_catch(img,region)
                    drag(loc)
                    gui.moveTo(100,100)
                
                    if keyboard.is_pressed('s'):
                        print('stop')
                        break
                    
            except gui.ImageNotFoundException:
                try:    
                    print('19')
                    img = './19.png'
                    while 1:
                        loc = screen_catch(img,region)
                        drag(loc)
                        gui.moveTo(100,100)
                    
                        if keyboard.is_pressed('s'):
                            print('stop')
                            break
                        
                except gui.ImageNotFoundException:
                        
                        try:    
                            print('82')
                            img = './82.png'
                            while 1:
                                loc = screen_catch(img,region)
                                drag(loc)
                                gui.moveTo(100,100)
                            
                                if keyboard.is_pressed('s'):
                                    print('stop')
                                    break
                                
                        except gui.ImageNotFoundException:
                            try:    
                                print('64')
                                img = './64.png'
                                while 1:
                                    loc = screen_catch(img,region)
                                    drag(loc)
                                    gui.moveTo(100,100)
                                
                                    if keyboard.is_pressed('s'):
                                        print('stop')
                                        break
                            except gui.ImageNotFoundException:
                                
                                try:    
                                    print('46')
                                    img = './46.png'
                                    while 1:
                                        loc = screen_catch(img,region)
                                        drag(loc)
                                        gui.moveTo(100,100)
                                    
                                        if keyboard.is_pressed('s'):
                                            print('stop')
                                            break
                                        
                                except gui.ImageNotFoundException:
                                    try:    
                                        print('55')
                                        img = './55.png'
                                        while 1:
                                            loc = screen_catch(img,region)
                                            drag(loc)
                                            gui.moveTo(100,100)
                                        
                                            if keyboard.is_pressed('s'):
                                                print('stop')
                                                break
                                    except gui.ImageNotFoundException:
                                        print('test')

print('test2')
try:    
    print('1.9')
    img = './1.9.png'
    while 1:
        loc = screen_catch(img,region)
        drag(loc)
        gui.moveTo(100,100)
    
        if keyboard.is_pressed('s'):
            print('stop')
            break
        
except gui.ImageNotFoundException:
        
        try:    
            print('8.2')
            img = './8.2.png'
            while 1:
                loc = screen_catch(img,region)
                drag(loc)
                gui.moveTo(100,100)
            
                if keyboard.is_pressed('s'):
                    print('stop')
                    break
                
        except gui.ImageNotFoundException:
            try:    
                print('6.4')
                img = './6.4.png'
                while 1:
                    loc = screen_catch(img,region)
                    drag(loc)
                    gui.moveTo(100,100)
                
                    if keyboard.is_pressed('s'):
                        print('stop')
                        break
            except gui.ImageNotFoundException:
                
                try:    
                    print('4.6')
                    img = './4.6.png'
                    while 1:
                        loc = screen_catch(img,region)
                        drag(loc)
                        gui.moveTo(100,100)
                    
                        if keyboard.is_pressed('s'):
                            print('stop')
                            break
                        
                except gui.ImageNotFoundException:
                    try:    
                        print('5.5')
                        img = './5.5.png'
                        while 1:
                            loc = screen_catch(img,region)
                            drag(loc)
                            gui.moveTo(100,100)
                        
                            if keyboard.is_pressed('s'):
                                print('stop')
                                break
                    except gui.ImageNotFoundException:
                        try:    
                            print('9.1')
                            img = './9.1.png'
                            while 1:
                                loc = screen_catch(img,region)
                                drag(loc)
                                gui.moveTo(100,100)
                            
                                if keyboard.is_pressed('s'):
                                    print('stop')
                                    break
                        except gui.ImageNotFoundException:
                            
                            try:    
                                print('2.8')
                                img = './2.8.png'
                                while 1:
                                    loc = screen_catch(img,region)
                                    drag(loc)
                                    gui.moveTo(100,100)
                                
                                    if keyboard.is_pressed('s'):
                                        print('stop')
                                        break
                                    
                            except gui.ImageNotFoundException:
                                try:    
                                    print('7.3')
                                    img = './7.3.png'
                                    while 1:
                                        loc = screen_catch(img,region)
                                        drag(loc)
                                        gui.moveTo(100,100)
                                    
                                        if keyboard.is_pressed('s'):
                                            print('stop')
                                            break
                                except gui.ImageNotFoundException:
                                    print('test3')
try:    
    print('3.7')
    img = './3.7.png'
    while 1:
        loc = screen_catch(img,region)
        drag(loc)
        gui.moveTo(100,100)
    
        if keyboard.is_pressed('s'):
            print('stop')
            break
        
except gui.ImageNotFoundException:
        
        try:    
            print('334')
            img = './334.png'
            while 1:
                loc = screen_catch(img,region)
                drag(loc)
                gui.moveTo(100,100)
            
                if keyboard.is_pressed('s'):
                    print('stop')
                    break
                
        except gui.ImageNotFoundException:
            print('end')                                    