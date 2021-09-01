# CONSTS
TITLE = "Halvors Eventyr"
WIDTH = 480
HEIGHT = 480
TILE_SIZE = 60

# RUN
import pygame as pg

pg.init()

pg.display.set_caption(TITLE)
screen = pg.display.set_mode((WIDTH, HEIGHT))

# GRAPHICS
halvor_left, halvor_right, halvor_front, halvor_back = pg.image.load("deps/halvor_left.png"), pg.image.load("deps/halvor_right.png"), pg.image.load("deps/halvor_front.png"), pg.image.load("deps/halvor_back.png")
halvor_left, halvor_right, halvor_front, halvor_back = pg.transform.scale(halvor_left, (TILE_SIZE, TILE_SIZE)), pg.transform.scale(halvor_right, (TILE_SIZE, TILE_SIZE)), pg.transform.scale(halvor_front, (TILE_SIZE, TILE_SIZE)), pg.transform.scale(halvor_back, (TILE_SIZE, TILE_SIZE))

flag = pg.image.load("deps/flag.png")
flag = pg.transform.scale(flag, (TILE_SIZE, TILE_SIZE))

grass = pg.image.load("deps/grass.png")
grass = pg.transform.scale(grass, (TILE_SIZE, TILE_SIZE))

hedge = pg.image.load("deps/hedge.png")
hedge = pg.transform.scale(hedge, (TILE_SIZE, TILE_SIZE))


win = pg.image.load("deps/win.png")
fail = pg.image.load("deps/fail.png")

def draw(tiles, halvor_pos, flag_pos, angle):
    global screen
    screen.fill((0, 0, 0))
    
    tiles_width, tiles_height = len(tiles[0]), len(tiles)
    camera_offset = ((WIDTH-tiles_width*TILE_SIZE)/2, (HEIGHT-tiles_height*TILE_SIZE)/2)
    
    for i in range(tiles_height):
        for j in range(tiles_width):
            tex = grass
            tile_pos = (j*TILE_SIZE + camera_offset[0], i*TILE_SIZE + camera_offset[1])
            
            if tiles[i][j] == 1:
                tex = hedge
            
            screen.blit(tex, tile_pos)
            
            if flag_pos[0] == j and flag_pos[1] == i:
                screen.blit(flag, tile_pos)
            
            if halvor_pos[0] == j and halvor_pos[1] == i:
                halvor = halvor_right
                if angle == 1:
                    halvor = halvor_front
                elif angle == 2:
                    halvor = halvor_left
                elif angle == 3:
                    halvor = halvor_back
                    
                screen.blit(halvor, tile_pos)
    
    pg.display.flip()

def drawWin():
    global screen
    screen.blit(win, (0,0))
    pg.display.flip()

def drawFail():
    global screen
    screen.blit(fail, (0,0))
    pg.display.flip()
