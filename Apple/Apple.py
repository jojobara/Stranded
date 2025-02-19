import cv2
import pytesseract
import pyautogui as gui
import numpy as np
from itertools import combinations
import time
import keyboard
from PIL import image

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
    gui.drag(box.width+10,box.height+10,duration=1.00)
    time.sleep(0.01)
    return                

filepath = 'C:\Pysp\Apple\Test.png'
pos = get_positions()
gui.screenshot(filepath, region = (pos[0].x, pos[0].y, pos[1].x-pos[0].x, pos[1].y- pos[0].y))

#a = image.open(filepath)
