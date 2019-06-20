#For a 270 rotated screen installed as a console
#x,y swapped for touch and y sense is inverted
#use python3 ./pygame_test.py on a keyboard direct connect to rpi
#with the touch lcd on it
#use python3 ./pygame_test.py on a keyboard direct connect to rpi
#with the touch lcd on it
#esc key when in the window will quit it, AFTER a touch event (because it blocks waiting for them)
 
import pygame, sys
import os
import time
import asyncio
import evdevTS
from pygame.locals import *
os.environ['SDL_VIDEODRIVER']='fbcon'
#os.environ['SDL_FBDEV']='/dev/fb0'   #fb0 works and higher res 640,320 but not all screen
os.environ['SDL_FBDEV']='/dev/fb1'   #fb1 works too but lower res 320 240 full screen
#os.environ['SDL_MOUSEDEV']='/dev/input/touchscreen'  #DONT'USE. BROKEN#
#os.environ['SDL_MOUSEDRV']='TSLIB' #This might be unneccessary...

tsfilename='/dev/input/touchscreen'
def main():
    pygame.init()
    WIDTH =320
    HEIGHT = 240
    AR= WIDTH/HEIGHT
    DISPLAY=pygame.display.set_mode((WIDTH,HEIGHT),0,32) #need smaller if using fb1
#    DISPLAY=pygame.display.set_mode((640,320),0,32) #if using fb0 this works

    WHITE=(255,255,255)
    BLUE=(0,0,255)
    RED=(255,0,0)

    DISPLAY.fill(WHITE)
    pygame.mouse.set_visible(False)
    pygame.draw.rect(DISPLAY,BLUE,(50,50,10,10))
    pygame.display.update()
    count=0
    finished = False
    tsdev = evdevTS.device(tsfilename)
    while True:
        x,y=evdevTS.get_touch_coords(tsdev)  #this blocks...
        oldx=x
        x = (y-300)/11    #OK evdev touchscreen needs rotation and scaling and offset
        y = HEIGHT-(oldx-300)/15  #there's an offset
        pygame.draw.rect(DISPLAY,RED,(x,y,10,10))
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    finished = True
            #if event.type == pygame.MOUSEBUTTONDOWN:   #But pygame touchscreen is inconsistant
                   #pos=event.pos
                   #print(pos, event.button)
                   #x=int(AR*pos[1])  #swap x and y
                   #y=int(HEIGHT-(pos[0])/AR)  #and invert y
                   #pygame.draw.rect(DISPLAY,BLUE,(x,y,10,10))
        
        count +=1
        if count > 1000 or finished == True:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        time.sleep(0.1)

main()
