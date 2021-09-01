import sys
import math
import time

import pygame as pg
from pygame.locals import QUIT

import deps.base

tiles = [[1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1]]

halvor_pos = [1, 2]
flag_pos = [6, 1]

angle = 1
game_ended = False

def updateScreen():
    global tiles, halvor_pos, flag_pos, angle
    deps.base.draw(tiles, halvor_pos, flag_pos, angle)
    time.sleep(0.5)

def win():
    global game_ended
    game_ended = True
    print("YOU PASSED")
    deps.base.drawWin()

def fail():
    global game_ended
    game_ended = True
    print("YOU FAILED")
    deps.base.drawFail()

def walkForward():
    global angle, pos, game_ended
    if game_ended:
        return
    
    angle_radians = math.radians(90*angle)
    
    direction = (round(math.cos(angle_radians)), round(math.sin(angle_radians)))
    
    halvor_pos[0] += direction[0]
    halvor_pos[1] += direction[1]
    
    updateScreen()
    
    if halvor_pos[0] < 0 or halvor_pos[0] >= len(tiles[0]) or halvor_pos[1] < 0 or halvor_pos[1] >= len(tiles): # OUT OF BOUNDS
        fail()
    elif tiles[halvor_pos[1]][halvor_pos[0]] == 1: # HIT SOMETHING
        fail()

def turnRight():
    global angle, game_ended
    if game_ended:
        return
    
    angle = (angle+1)%4
    updateScreen()

def turnLeft():
    global angle, game_ended
    if game_ended:
        return
    angle = (angle-1)%4
    updateScreen()

def validate():
    if halvor_pos == flag_pos:
        win()
    
    if not game_ended:
        fail()
    
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()        

print("==Halvors Eventyr - Post 1==")
updateScreen()
time.sleep(0.75)