import sys
import pygame as pg
from world import world
from entity import player
from constants import WINDOW_SIZE, DIRECTION, CONTROLS

def init():
    w = world('assets/level.dat')
    w.addEntitiy(player(pos=[3,3], image='assets/pika.png'))
    screen = pg.display.set_mode(WINDOW_SIZE)

    def update():
        for e in pg.event.get():
            if e.type == pg.QUIT: sys.exit()
            if e.type == pg.KEYDOWN:
                w.update(e)

    def draw():
        w.draw(screen)
        pg.display.flip()  

    return update, draw

if __name__ == '__main__':
    pg.init()
    update, draw = init()
    while 1:       
        update()
        draw()

