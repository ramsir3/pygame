import sys
import pygame as pg
from world import world
from entity import player
from constants import WINDOW_SIZE, DIRECTION, CONTROLS

pg.init()

w = world('assets/level.dat')
p = player(pos=[3,3], world=w)
screen = pg.display.set_mode(WINDOW_SIZE)

def update():
    for e in pg.event.get():
        if e.type == pg.QUIT: sys.exit()
        if e.type == pg.KEYDOWN:
            if e.key in CONTROLS:
                p.move(CONTROLS[e.key])
                print(p.pos)

def draw():
    w.draw(screen)
    p.draw(screen)
    pg.display.flip()
    pass    

while 1:       
    update()
    draw()

